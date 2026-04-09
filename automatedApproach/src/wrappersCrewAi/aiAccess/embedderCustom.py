class NoOpEmbedder:
    '''satisfies the crewai embedder interface but has no real functionality; could be expanded in the furture for acctual memory management'''
    def __call__(self, text: str) -> list[float]:
        return []