from typing import Any

class AiAccessInterface:
    # This class serves as an interface for connecting to an AI browser or terminal. It defines the methods that must be implemented by any subclass that wants to provide access to an AI service.
    def __init__(self) -> None:
        self.connection = None

    def sayHello(self) -> None:
        # This method can be used to greet the user or perform any initialization tasks.
        raise NotImplementedError("Subclasses must implement this method.")
    
    def connect(self, model: str) -> bool:
        # This method should be implemented by subclasses to establish a connection to the AI browser.
        raise NotImplementedError("Subclasses must implement this method.") 

    def ask(self, model : str, modelsGeneralPurpose : str, questionTheModelShouldWorkOn : str, previousModelsWork, reasoningEffort :str = "medium")-> tuple[dict[str, Any], str]:
        # This method should be implemented by subclasses to send a prompt to the AI and receive a response.
        raise NotImplementedError("Subclasses must implement this method.") 
    
    def disconnect(self) -> bool:
        # This method should be implemented by subclasses to disconnect from the AI service.
        raise NotImplementedError("Subclasses must implement this method.") 
    