from aiAccessInterface import AiAccessInterface
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
            base_url="https://chat-ai.academiccloud.de/v1"
        )

    def sayHello(self) -> None:
        # This method can be used to greet the user
        print("Hello! This is the AiAccessTerminal class.")

    def listModels(self):
        # This method can be used to list available models from the AI service.
        models = self.client.models.list()
        for m in models.data:
            print(m.id)
    
    def connect(self) -> bool:
        # This method can be used to perform any initialization tasks or checks before sending requests.
        return self.ask("this is a connection check. Please respond with 'Connection successful!' if the connection is working properly.", model="llama-3.3-70b-instruct")

    def ask(self, prompt : str, model : str ="llama-3.3-70b-instruct") -> str:
        # This method sends a prompt to the AI and receives a response. It uses the OpenAI client to create a chat completion.
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content
        print(f"AI response: {answer}")
        return answer
    
    def disconnect(self)-> bool:
        # This method can be used to perform any cleanup tasks or close connections if necessary.
        # Since this is a terminal-based access, there might not be any persistent connections to close.
        print("Disconnecting from terminal AI access, by setting the API key to None.")
        self.client.api_key = None
        return True