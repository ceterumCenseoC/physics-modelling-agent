# module-level wrapper (save as a .py file and import it)
from typing import List
from src.wrappersCrewAi.aiAccess.embedderCustom import EmbedderCustom
import os

# instantiate the embedder once at module import time
import os
from dotenv import load_dotenv
from pathlib import Path
env_path = Path(__file__).resolve().parent.parent.parent.parent / ".env" # set the path to the .env file
load_dotenv(dotenv_path=env_path)
# normalize your key
apiKey = os.getenv("API_KEY", "").strip()

_embedder = EmbedderCustom(model="e5-mistral-7b-instruct")

def module_embed(texts: List[str]) -> List[List[float]]:
    """Module-level callable that WebsiteSearchTool can serialize/validate."""
    # optional logging for diagnostics
    print("MODULE EMBED called with", len(texts), "texts")
    return _embedder.embed(texts)
