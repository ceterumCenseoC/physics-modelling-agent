from typing import Optional, Type, List
import os
import json
from pathlib import Path
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

try:
    import fitz  # PyMuPDF
except Exception:
    fitz = None


class PDFReaderInput(BaseModel):
    path: str = Field(..., description="Path to a PDF file or directory. Default should be used")
    recursive: bool = Field(False, description="Search subdirectories if True.")
    max_files: Optional[int] = Field(None, description="Optional cap on number of files.")

class PDFReader(BaseTool):
    name: str = "pdf_reader"
    description: str = "Read all PDF files in a directory and return extracted text."
    args_schema: Type[BaseModel] = PDFReaderInput
    read_path: str = "./arxiv_pdfs" # default path, can be overridden

    run_identifier: str = "0"  # default value, can be overridden

    def _gather(self, p: Path, recursive: bool, max_files: Optional[int] = 5) -> List[Path]:
        if p.is_file():
            return [p] if p.suffix.lower() == ".pdf" else []
        if not p.exists() or not p.is_dir():
            return []
        it = p.rglob("*.pdf") if recursive else p.glob("*.pdf")
        files = []
        for f in it:
            if f.is_file():
                files.append(f)
                if max_files and len(files) >= max_files:
                    break
        return files

    def _extract(self, file_path: Path) -> str:
        if fitz is None:
            raise RuntimeError("PyMuPDF (fitz) is required.")
        doc = fitz.open(str(file_path))
        try:
            texts = []
            for i in range(len(doc)):
                page = doc.load_page(i)
                texts.append(page.get_text("text") or "")
            return "\n\n".join(texts).strip()
        finally:
            doc.close()

    def _run(self, path: str = read_path, recursive: bool = False, max_files: Optional[int] = None) -> str:
        #p = Path(os.path.abspath(os.path.expanduser(path)))
        #source_dir = Path(__file__).resolve().parent.parent.parent.parent / "arxiv_pdfs" / f"runNr_{self.run_identifier}"
        if path != self.read_path:
            path = self.read_path    
        source_dir = Path(path) / f"runNr_{self.run_identifier}"
        print(f"PDFReader: Gathering PDF files from {source_dir}")

        files = self._gather(source_dir, recursive, max_files)
        results = []
        for f in files:
            try:
                text = self._extract(f)
            except Exception as e:
                results.append({"file_path": str(f), "error": str(e)})
            else:
                results.append({"file_path": str(f), "full_text": text})
        return json.dumps({"path": str(source_dir), "files_found": len(files), "results": results}, ensure_ascii=False)
