from typing import Any

from .aiAccessInterface import AiAccessInterface
class AiAccessTerminal(AiAccessInterface):
    # This class provides an interface to access an AI service through a terminal-based approach. It uses the OpenAI API to send prompts and receive responses from the AI models.
    def __init__(self) -> None:
        import os
        from dotenv import load_dotenv
        from pathlib import Path
        env_path = Path(__file__).resolve().parent.parent / ".env"  # aiWorkflow/.env
        load_dotenv(dotenv_path=env_path)
        apiKey = os.getenv("API_KEY")
        import openai
        self.client = openai.OpenAI(
            api_key=apiKey,
            base_url="https://saia.gwdg.de/v1"#"https://chat-ai.academiccloud.de/v1"
        )

    def sayHello(self) -> None:
        # This method can be used to greet the user
        print("Hello! This is the AiAccessTerminal class.")

    def listModels(self) -> list:
        # This method can be used to list available models from the AI service.
        models = self.client.models.list()
        modelList : list[str] = []
        for m in models.data:
            modelList.append(m.id)
        return modelList

    def connect(self, model : str) -> bool:
        # This method can be used to perform any initialization tasks or checks before sending requests.
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": "this is a connection check. Please respond with 'Connection successful!' if the connection is working properly."
                }
            ]
        )

        return response.choices[0].message.content.strip() == "Connection successful!"

    
    def ask(self, model : str, modelsGeneralPurpose : str, questionTheModelShouldWorkOn : str, previousModelsWork, reasoningEffort :str = "medium")-> tuple[dict[str, Any], str]:
        # This method sends a prompt to the AI and receives a response. It uses the OpenAI client to create a chat completion.
        response = self.client.chat.completions.create(
            model=model,
            reasoning_effort = reasoningEffort,
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": modelsGeneralPurpose
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": questionTheModelShouldWorkOn
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": previousModelsWork
                        }
                    ]
                }
            ],
            response_format = {
                "type": "json_schema",
                "json_schema": {
                    "name": "model_output",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "answer": {"type": "string"},
                            "confidence": {"type": "number"}
                        },
                        "required": ["answer", "confidence"],
                        "additionalProperties": False
                    }
                }
            }
        )
        print(str(response))
        #answer = response.output #sould return json format
        responseId = response.id
        return responseId
    
    def disconnect(self)-> bool:
        # This method can be used to perform any cleanup tasks or close connections if necessary.
        # Since this is a terminal-based access, there might not be any persistent connections to close.
        print("Disconnecting from terminal AI access, by setting the API key to None.")
        self.client.api_key = None
        return True

if __name__ == "__main__":
    ai_access = AiAccessTerminal()
    ai_access.sayHello()
    models = ai_access.listModels()
    print("Available models:", models)
    ai_access.ask(model="deepseek-v4-flash-0731", modelsGeneralPurpose="You are a helpful assistant.", questionTheModelShouldWorkOn="What is the capital of France?", previousModelsWork="")