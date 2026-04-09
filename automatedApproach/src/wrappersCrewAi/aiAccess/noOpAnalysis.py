class NoOpAnalysis:
    def __init__(self) -> None:
        pass

    def call(self, *args, **kwargs) -> None:
        return None