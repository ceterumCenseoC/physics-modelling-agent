import os
import re
from pathlib import Path
import requests
from crewai_tools import ArxivPaperTool

class ArxivSearch(ArxivPaperTool):
    def _run(self, search_query, max_results=1):
        raw = super()._run(search_query, max_results)

        # --- Extract title robustly ---
        title_match = re.search(r"Title:\s*(.+)", raw)
        if title_match:
            title = title_match.group(1).strip()
            title = re.sub(r"[^\w\-]+", "_", title)  # sanitize filename
            title = title[:40] # limit length
        else:
            title = "arxiv_paper"

        # --- Extract PDF URL robustly ---
        pdf_match = re.search(r"PDF:\s*(https?://\S+)", raw)
        if pdf_match:
            pdf_url = pdf_match.group(1).strip()
        else:
            return {"error": "Could not extract PDF URL", "raw_output": raw}

        # --- Save directory ---
        base_dir = Path(__file__).resolve().parent.parent.parent.parent # should be set by user from outside

        output_dir = (
            base_dir / "arxiv_papers"
        )
        os.makedirs(output_dir, exist_ok=True)

        pdf_path = os.path.join(output_dir, f"{title}.pdf")

        # --- Download PDF ---
        r = requests.get(pdf_url)
        with open(pdf_path, "wb") as f:
            f.write(r.content)

        return {
            "saved_pdf": pdf_path,
            "pdf_url": pdf_url,
            "title": title,
            "raw_metadata": raw
        }
