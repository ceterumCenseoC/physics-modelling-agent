import requests
from typing import List
from dotenv import load_dotenv

class EmbedderCustom:
    """
    Minimal wrapper that exposes embed(texts: List[str]) -> List[List[float]]
    - Strips the API key
    - Batches requests
    - Raises on non-2xx responses
    """
    def __init__(self,  model: str = "E5-mistral-7b-instruct", api_key: str = "", endpoint: str = "https://chat-ai.academiccloud.de/v1", batch_size: int = 32, timeout: int = 30) -> None:
        self.endpoint = endpoint.rstrip("/")
        self.model = model
        self.batch_size = batch_size
        self.timeout = timeout
        self.api_key = api_key
        if self.api_key == "":
            import os
            from dotenv import load_dotenv
            from pathlib import Path
            env_path = Path(__file__).resolve().parent / ".env" # set the path to the .env file
            load_dotenv(dotenv_path=env_path)
            apiKey = os.getenv("OPENAI_API_KEY") # read the API_KEY from the .env file
            self.api_key = apiKey

    def _post_embeddings(self, inputs: List[str]) -> List[List[float]]:
        url = f"{self.endpoint}/embeddings"
        payload = {"model": self.model, "input": inputs}
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        print("DEBUG: embedding POST URL:", f"{self.endpoint.rstrip('/')}/embeddings")
        print("DEBUG: Authorization header prefix:", f"Bearer {self.api_key[:8]}...")
        print("DEBUG: payload sample:", {"model": self.model, "input": inputs[:2]})


        resp = requests.post(url, json=payload, headers=headers, timeout=self.timeout)
        resp.raise_for_status()
        data = resp.json()
        # Adjust the path below to match SAIA's response shape
        # Common shapes: {"data":[{"embedding":[...]}]} or {"embeddings":[[...]]}
        if "data" in data and isinstance(data["data"], list) and "embedding" in data["data"][0]:
            return [item["embedding"] for item in data["data"]]
        if "embeddings" in data:
            return data["embeddings"]
        # Fallback: try to find first list-of-floats in response
        for v in data.values():
            if isinstance(v, list) and v and isinstance(v[0], list):
                return v
        raise ValueError("Unexpected embeddings response shape: " + str(data))

    def embed(self, texts: List[str]) -> List[List[float]]:
        print("DEBUG: EMBEDDING NOW")
        if not texts:
            return []
        embeddings: List[List[float]] = []
        for i in range(0, len(texts), self.batch_size):
            batch = texts[i : i + self.batch_size]
            embeddings.extend(self._post_embeddings(batch))
        return embeddings

    # Optional helper to test connectivity
    def health_check(self) -> bool:
        try:
            # If SAIA exposes a models or health endpoint, call it; otherwise do a small embed
            self._post_embeddings(["test"])
            return True
        except Exception:
            return False
