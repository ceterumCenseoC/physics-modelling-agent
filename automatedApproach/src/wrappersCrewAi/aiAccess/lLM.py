from src.wrappersCrewAi.aiAccess.openAiClient import OpenAiClient

class LLM:
    def __init__(self, client: OpenAiClient, model: str) -> None:
        self.client = client
        self.model = model
        self._token_usage = None
        self.supports_function_calling = False

    def call(self, messages, **kwargs) -> str:
        model = str(kwargs.get("model", self.model))
        answer = self.client.run(model=model, messages=messages, **kwargs)
        self.usage = answer["usage"]
        self._token_usage = {
            "input_tokens": getattr(self.usage, "prompt_tokens", None),
            "output_tokens": getattr(self.usage, "completion_tokens", None),
            "total_tokens": getattr(self.usage, "total_tokens", None),
        }
        return answer["content"]