# utils/config.py
from pathlib import Path
import yaml
import os
import re

_env_pattern = re.compile(r"\$\{([^}]+)\}")

def _expand_env(obj):
    if isinstance(obj, str):
        return _env_pattern.sub(lambda m: os.getenv(m.group(1), ""), obj)
    if isinstance(obj, dict):
        return {k: _expand_env(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_expand_env(v) for v in obj]
    return obj

def load_yaml(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"{path} not found")
    if p.is_dir():
        merged = {}
        for f in sorted(p.glob("*.yaml")):
            with f.open("r", encoding="utf-8") as fh:
                data = yaml.safe_load(fh) or {}
            merged.update(_expand_env(data))
        return merged
    else:
        with p.open("r", encoding="utf-8") as fh:
            return _expand_env(yaml.safe_load(fh) or {})
