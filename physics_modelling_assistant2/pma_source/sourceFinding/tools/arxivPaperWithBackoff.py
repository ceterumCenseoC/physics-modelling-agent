import os
import logging
from pathlib import Path
import random
import re
import time
from typing import Any, ClassVar
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from crewai.tools import BaseTool, EnvVar
from pydantic import BaseModel, ConfigDict, Field


logger = logging.getLogger(__file__)


class ArxivToolInput(BaseModel):
    search_query: str = Field(
        ..., description="Search query for Arxiv, e.g., 'transformer neural network'"
    )
    max_results: int = Field(
        5, ge=1, le=6, description="Max results to fetch; must be between 1 and 10"
    )
    max_retries: int = Field(
        5, ge=1, le=10, description="Max retries for API calls; must be between 1 and 10"
    )
    base_delay: float = Field(
        4.0, ge=4.0, le=10.0, description="Base delay for backoff strategy; must be between 4.0 and 10.0"
    )


class ArxivPaperTool(BaseTool):
    BASE_API_URL: ClassVar[str] = "http://export.arxiv.org/api/query"
    SLEEP_DURATION: ClassVar[int] = 1
    SUMMARY_TRUNCATE_LENGTH: ClassVar[int] = 300
    ATOM_NAMESPACE: ClassVar[str] = "{http://www.w3.org/2005/Atom}"
    REQUEST_TIMEOUT: ClassVar[int] = 50
    name: str = "Arxiv Paper Fetcher and Downloader"
    description: str = "Fetches metadata from Arxiv based on a search query and optionally downloads PDFs."
    args_schema: type[BaseModel] = ArxivToolInput
    model_config = ConfigDict(extra="allow")
    package_dependencies: list[str] = Field(default_factory=lambda: ["pydantic"])
    env_vars: list[EnvVar] = Field(default_factory=list)
    download_pdfs: bool = True # want that
    save_dir: str = "./arxiv_pdfs"
    use_title_as_filename: bool = True # yes
    def _run(self, search_query: str, max_results: int = 5, max_retries: int = 10, base_delay: float = 4.0) -> str:
        try:
            args = ArxivToolInput(search_query=search_query, max_results=max_results, max_retries=max_retries, base_delay=base_delay)
            logger.info(
                f"Running Arxiv tool: query='{args.search_query}', max_results={args.max_results}, "
                f"download_pdfs={self.download_pdfs}, save_dir='{self.save_dir}', "
                f"use_title_as_filename={self.use_title_as_filename}"
            )

            papers = self.fetch_arxiv_data(args.search_query, args.max_results, args.max_retries, args.base_delay)
            successfully_downloaded_pdfs = []

            if self.download_pdfs:
                save_dir = self._validate_save_path(self.save_dir)
                for paper in papers:
                    if paper["pdf_url"]:
                        if self.use_title_as_filename:
                            safe_title = re.sub(
                                r'[\\/*?:"<>|]', "_", paper["title"]
                            ).strip()
                            filename_base = safe_title or paper["arxiv_id"]
                        else:
                            filename_base = paper["arxiv_id"]
                        filename = f"{filename_base[:100]}.pdf" # Truncate to 100 chars to avoid filesystem issues (max path length)
                        save_path = Path(save_dir) / filename

                        success = self.download_pdf(paper["pdf_url"], save_path)  # type: ignore[arg-type]
                        if success:
                            successfully_downloaded_pdfs.append(paper)
                        num_files = sum(
                            1 for entry in os.scandir(save_dir)
                            if entry.is_file()
                        )

                        if len(successfully_downloaded_pdfs) >= args.max_results or num_files >= args.max_results: # if max_results is reached, stop downloading; due to the arxivAPI return, more than max_results papers can be returned
                            # this will probably cause context window exceeding issues, so we stop downloading after max_results
                            results = [self._format_paper_result(p) for p in successfully_downloaded_pdfs]
                            return "\n\n" + "-" * 80 + "\n\n".join(results)
                            
                        time.sleep(self.SLEEP_DURATION)

            results = [self._format_paper_result(p) for p in successfully_downloaded_pdfs]
            return "\n\n" + "-" * 80 + "\n\n".join(results)

        except Exception as e:
            logger.error(f"ArxivTool Error: {e!s}")
            return f"Failed to fetch or download Arxiv papers: {e!s}"

    def fetch_arxiv_data(
        self, search_query: str, max_results: int, max_retries: int, base_delay: float
    ) -> list[dict[str, Any]]:
        api_url = f"{self.BASE_API_URL}?search_query={urllib.parse.quote(search_query)}&start=0&max_results={max_results}"
        logger.info(f"Fetching data from Arxiv API: {api_url}")

        success = False
        data = ""

        for attempt in range(max_retries):
            print(f"Attempt {attempt + 1} of {max_retries} to fetch data from Arxiv API...")
            try:
                req = urllib.request.Request(
                    api_url,
                    headers={"User-Agent": "MyArxivClient/1.0 (mailto:your-email@example.com)"}
                )
                with urllib.request.urlopen(req, timeout=self.REQUEST_TIMEOUT) as response:
                    if response.status != 200:
                        raise Exception(f"HTTP {response.status}: {response.reason}")
                    data = response.read().decode("utf-8")
                    success = True
                    break  # Exit loop on success

            except urllib.error.HTTPError as e:
                # Respect Retry-After if present
                print(f"HTTP error occurred: {e.code} {e.reason}. Retrying...")
                retry_after = e.headers.get("Retry-After")
                if retry_after:
                    time.sleep(int(retry_after))
                    continue

                if attempt == max_retries - 1:
                    raise

                # Exponential backoff with jitter
                delay = base_delay * (2 ** attempt)
                delay = delay * (1 + random.uniform(0, 0.3))
                time.sleep(delay)

            except urllib.error.URLError as e:
                print(f"Network error occurred: {e.reason}. Retrying in {base_delay} seconds...")
                if attempt == max_retries - 1:
                    raise
                delay = base_delay * (2 ** attempt)
                delay = delay * (1 + random.uniform(0, 0.3))
                time.sleep(delay)

        if success:
            print("Successfully fetched data from Arxiv API.")
            time.sleep(base_delay)  # Sleep after successful fetch to be polite to the API

        root = ET.fromstring(data)  # noqa: S314
        papers = []

        for entry in root.findall(self.ATOM_NAMESPACE + "entry"):
            raw_id = self._get_element_text(entry, "id")
            arxiv_id = raw_id.split("/")[-1].replace(".", "_") if raw_id else "unknown"

            title = self._get_element_text(entry, "title") or "No Title"
            summary = self._get_element_text(entry, "summary") or "No Summary"
            published = self._get_element_text(entry, "published") or "No Publish Date"
            authors = [
                self._get_element_text(author, "name") or "Unknown"
                for author in entry.findall(self.ATOM_NAMESPACE + "author")
            ]

            pdf_url = self._extract_pdf_url(entry)

            papers.append(
                {
                    "arxiv_id": arxiv_id,
                    "title": title,
                    "summary": summary,
                    "authors": authors,
                    "published_date": published,
                    "pdf_url": pdf_url,
                }
            )

        return papers

    @staticmethod
    def _get_element_text(entry: ET.Element, element_name: str) -> str | None:
        elem = entry.find(f"{ArxivPaperTool.ATOM_NAMESPACE}{element_name}")
        return elem.text.strip() if elem is not None and elem.text else None

    def _extract_pdf_url(self, entry: ET.Element) -> str | None:
        for link in entry.findall(self.ATOM_NAMESPACE + "link"):
            if link.attrib.get("title", "").lower() == "pdf":
                return link.attrib.get("href")
        for link in entry.findall(self.ATOM_NAMESPACE + "link"):
            href = link.attrib.get("href")
            if href and "pdf" in href:
                return href
        return None

    def _format_paper_result(self, paper: dict[str, Any]) -> str:
        summary = (
            (paper["summary"][: self.SUMMARY_TRUNCATE_LENGTH] + "...")
            if len(paper["summary"]) > self.SUMMARY_TRUNCATE_LENGTH
            else paper["summary"]
        )
        authors_str = ", ".join(paper["authors"])
        return (
            f"Title: {paper['title']}\n"
            f"Authors: {authors_str}\n"
            f"Published: {paper['published_date']}\n"
            f"PDF: {paper['pdf_url'] or 'N/A'}\n"
            f"Summary: {summary}"
        )

    @staticmethod
    def _validate_save_path(path: str) -> Path:
        save_path = Path(path).resolve()
        save_path.mkdir(parents=True, exist_ok=True)
        return save_path

    def download_pdf(self, pdf_url: str, save_path: str) -> bool:
        try:
            logger.info(f"Downloading PDF from {pdf_url} to {save_path}")
            urllib.request.urlretrieve(pdf_url, str(save_path))  # noqa: S310
            logger.info(f"PDF saved: {save_path}")
            return True
        except urllib.error.URLError as e:
            logger.error(f"Network error occurred while downloading {pdf_url}: {e}")
            raise
            return False
        except OSError as e:
            logger.error(f"File save error for {save_path}: {e}")
            raise
            return False
        except urllib.error.HTTPError as e:
            logger.error(f"HTTP error occurred while downloading {pdf_url}: {e.code} {e.reason}")
            raise
            return False
        except Exception as e:
            logger.error(f"Unexpected error occurred while downloading {pdf_url}: {e}")
            raise
            return False