import openai
import sys

class OpenAiClient:
    def __init__(self) -> None:
        import os
        from dotenv import load_dotenv
        from pathlib import Path
        env_path = Path(__file__).resolve().parent.parent.parent.parent / ".env" 
        load_dotenv(dotenv_path=env_path)
        apiKey = os.getenv("API_KEY")
        self.client = openai.OpenAI(
            api_key=apiKey,
            base_url="https://chat-ai.academiccloud.de/v1"
        )

    def run(self, model: str, **kwargs) -> str:

        messages = kwargs.get("messages", [])

        context = str(kwargs.get("context", "")) #NOT OPENAI SUPPORTED

        tools = (kwargs.get("tools", []))
        available_functions = str(kwargs.get("available_functions", []))

        temperature = float(kwargs.get("temperature", 0.1))
        max_tokens = int(kwargs.get("max_tokens", 260000))
        stop = str(kwargs.get("stop", None))
        response_format = str(kwargs.get("response_format", "text")) # can be "text", "json", "xml", etc. depending on the use case and the capabilities of the connected AI; can also be a custom function that processes the raw response from the AI and formats it accordingly; not implemented yet

        stream = bool(kwargs.get("stream", False)) # whether to stream the response from the AI or not; not implemented yet
        callbacks = kwargs.get("callbacks", []) # callbacks for different stages of the LLM's reasoning process, e.g. before/after API call, before/after response processing, NOT OPENAI SUPPORTED


        self.__init__() # re-initialize the client for each call to avoid issues with rate limits and connection drops; not the most efficient way but works for now; can be optimized later by implementing a more sophisticated retry mechanism with exponential backoff, connection pooling, etc.
        response = self.client.chat.completions.create(
            messages=messages,
            model = model,
            tools=tools,
            temperature=temperature,
            max_tokens=max_tokens,
            stop=stop,
            response_format={"type": response_format},
            stream=stream,
            )

        return {"content" : response.choices[0].message.content,
                "usage" : response.usage
            }