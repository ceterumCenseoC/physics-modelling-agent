from src.crewAi.aiAccess.openAiClient import OpenAiClient
from crewai.llms.base_llm import BaseLLM

class LLM(BaseLLM):
    def __init__(self, client : OpenAiClient, model: str) -> None:
        self.client : OpenAiClient = client #an instance of the OpenAI client
        self.model : str = model
        self._token_usage : dict = None #to store token usage information after a call to the run method; includes input_tokens, output_tokens, total_tokens


    def call(self, messages, **kwargs) -> str:
        model = str(kwargs.get("model", self.model))
        answer = self.client.run(model=model, messages = messages, **kwargs)
        self.usage = answer["usage"]
        self._token_usage = {
            "input_tokens": self.usage.prompt_tokens,
            "output_tokens": self.usage.completion_tokens,
            "total_tokens": self.usage.total_tokens
        }
        return answer["content"]