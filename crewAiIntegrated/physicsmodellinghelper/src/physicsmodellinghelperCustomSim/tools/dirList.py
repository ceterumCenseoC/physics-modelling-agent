import os
import json
from typing import Optional, Type, List
from pathlib import Path
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class DirectoryListerInput(BaseModel):
    """Input schema for DirectoryListerTool."""
    path: str = Field(..., description="Absolute or relative path to a file or directory to inspect.")
    recursive: bool = Field(False, description="If true and path is a directory, walk subdirectories.")
    max_depth: Optional[int] = Field(None, description="Maximum recursion depth when recursive=True. None = unlimited.")
    allowed_base: Optional[str] = Field(None, description="Optional allowlist base directory. If set, path must be inside this base.")
    sample_limit: int = Field(20, description="Number of sample entries to return per directory.")

class DirectoryListerTool(BaseTool):
    """
    CrewAI-compatible tool that lists directories and files visible to the agent runtime.
    Returns a JSON string with diagnostics (resolved path, existence, permissions) and
    a list of discovered directories (with sample entries).
    """
    name: str = "directory_lister"
    description: str = "List directories and sample entries for a given path; useful for runtime visibility diagnostics."
    args_schema: Type[BaseModel] = DirectoryListerInput

    def _is_within_base(self, resolved: Path, base: Optional[str]) -> bool:
        if not base:
            return True
        try:
            base_p = Path(base).expanduser().resolve()
            resolved.relative_to(base_p)
            return True
        except Exception:
            return False

    def _gather(self, start: Path, recursive: bool, max_depth: Optional[int], sample_limit: int):
        results = []
        start_depth = len(start.resolve().parts)
        if start.is_file():
            parent = start.parent
            try:
                entries = os.listdir(parent)[:sample_limit]
            except Exception as e:
                entries = []
                error = str(e)
            else:
                error = None
            results.append({
                "path": str(parent),
                "is_dir": True,
                "sample_entries": entries,
                "error": error
            })
            return results

        # start is directory
        for root, dirs, files in os.walk(start):
            depth = len(Path(root).resolve().parts) - start_depth
            results.append({
                "path": str(Path(root).resolve()),
                "is_dir": True,
                "sample_entries": (dirs + files)[:sample_limit],
                "error": None
            })
            if not recursive:
                break
            if max_depth is not None and depth >= max_depth:
                # do not descend further
                # prune walk by clearing dirs
                dirs.clear()
        return results

    def _run(
        self,
        path: str,
        recursive: bool = False,
        max_depth: Optional[int] = None,
        allowed_base: Optional[str] = None,
        sample_limit: int = 20,
    ) -> str:
        # Normalize and resolve path
        if not isinstance(path, str) or not path.strip():
            return json.dumps({"error": "invalid_path", "message": "path must be a non-empty string"}, ensure_ascii=False)

        p = Path(path).expanduser()
        try:
            resolved = p.resolve()
        except Exception:
            # fallback to normalized string if resolve fails (e.g., permission)
            resolved = p

        debug = {
            "original_path": path,
            "resolved_path": str(resolved),
            "cwd": os.getcwd(),
            "exists": resolved.exists() if isinstance(resolved, Path) else False,
            "is_dir": resolved.is_dir() if isinstance(resolved, Path) and resolved.exists() else False,
            "allowed_base": allowed_base,
        }

        # Enforce allowlist if provided
        if allowed_base:
            if not self._is_within_base(resolved, allowed_base):
                return json.dumps({"error": "path_not_allowed", **debug}, ensure_ascii=False)

        if not resolved.exists():
            return json.dumps({"error": "path_not_found", **debug}, ensure_ascii=False)

        try:
            results = self._gather(resolved, recursive, max_depth, sample_limit)
        except PermissionError as e:
            debug["list_error"] = str(e)
            return json.dumps({"error": "permission_denied", **debug}, ensure_ascii=False)
        except Exception as e:
            debug["list_error"] = str(e)
            return json.dumps({"error": "unexpected_error", **debug}, ensure_ascii=False)

        output = {
            "debug": debug,
            "directories_found": len(results),
            "results": results
        }
        return json.dumps(output, ensure_ascii=False, indent=2)
