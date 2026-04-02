class NoOpEmbedder:
    def __call__(self, text: str) -> list[float]:
        return []