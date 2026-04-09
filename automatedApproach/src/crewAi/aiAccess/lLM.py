from src.crewAi.aiAccess.openAiClient import OpenAiClient
from crewai.llms.base_llm import BaseLLM

class LLM(BaseLLM):
    '''inherits from the BaseLLM class from crewai; interface for custom LLM use'''
    def __init__(self, client : OpenAiClient, model: str) -> None:
        '''initializes the LLM instance with the parameters required of the interface by crewai'''
        self.client : OpenAiClient = client #an instance of the OpenAI client, handles the acctual API call
        self.model : str = model # the model to use for the LLM
        self._token_usage : dict = None #to store token usage information after a call to the run method; includes input_tokens, output_tokens, total_tokens; REQUIRED BY CREWAI INTERFACE

    def call(self, messages, **kwargs) -> str:
        '''required method by crewai; gets called like that and takes messages and multiple other parameters'''
        model = str(kwargs.get("model", self.model)) # read out the model from the kwargs, the model is then seperately passed to the LLM instance
        answer = self.client.run(model=model, messages = messages, **kwargs) # call the run method of the OpenAi client: model and messages are specified; messages is a json-style dict. kwargs is just passed down
        self.usage = answer["usage"] # stores token usage info from API call.
        self._token_usage = { # assign the token usage to the token usage attribute
            "input_tokens": self.usage.prompt_tokens,
            "output_tokens": self.usage.completion_tokens,
            "total_tokens": self.usage.total_tokens
        }
        return answer["content"]