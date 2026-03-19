from typing import Any
from src.pipelineStepEnum import PipelineStepEnum
from src.aiAccessInterface import AiAccessInterface

class ControllAI:
    def __init__(self, name : str, modelsGeneralPurpose : str, model : str = None) -> None:
        self.name : str = name
        self.connection : AiAccessInterface = None
        self.model : str = model #the model that will be used for requests
        self.generalPurpose : str = modelsGeneralPurpose # gets fed into model with the role "SYSTEM"
        self.functionInPipeline : PipelineStepEnum.PipelineStepEnum = None #gets labeled according to the definded steps of the pipeline

    def sayHello(self) -> None:
        print(f"Hello, I am {self.name}!")

    def connectToAi(self, browser: bool = False) -> bool:
        '''establishes the connection. If browser is true, it will connect to the browserAI, otherwise to the terminalAI; does NOT set a first model, because an overview of models can be retrieved without a model needed'''        
        if browser:
            from src.aiAccessBrowser import AiAccessBrowser
            self.connection = AiAccessBrowser()
        else:
            from src.aiAccessTerminal import AiAccessTerminal
            self.connection = AiAccessTerminal()
        return True
    
    def checkConnection(self, model : str = None) -> bool:
        '''checks wheter a test prompt works and sets a default model'''
        if model is None:
            if self.model is None:
                self.model = self.connection.listModel[0]
            return self.connection.connect(self.model)
        return self.connection.connect(model)

    def listModels(self) -> list:
        '''only works for terminal'''
        if self.connection is None:
            self.connectToAi()
        return self.connection.listModels()
    
    def ask(self, promt : str, questionTheModelShouldWorkOn : str, previousModelsWork : str, modelsGeneralPurpose : str = None, model : str = None, reasoningEffort : str = None) -> tuple[dict[str, Any], str]:
        if self.connection is None:
            self.connectToAi(browser=False) # makes sure, a Model exists

        if modelsGeneralPurpose is None:
            modelsGeneralPurpose = self.generalPurpose # must be set by default

        if model is None: # when no model is specified
            if self.model is None: #rely on the model attribut, but if this is also None
                self.checkConnection() # perform checkConnection(), which sets the model attribute to a default value
            model = self.model
        
        answer = None

        if reasoningEffort is None:
            answer = self.connection.ask(self, model, modelsGeneralPurpose = modelsGeneralPurpose, questionTheModelShouldWorkOn = questionTheModelShouldWorkOn, previousModelsWork = previousModelsWork)
        else:
            answer = self.connection.ask(self, model, modelsGeneralPurpose = modelsGeneralPurpose, questionTheModelShouldWorkOn = questionTheModelShouldWorkOn, previousModelsWork = previousModelsWork, reasoningEffort = reasoningEffort)
        
        return answer

    def diconnect(self) -> bool:
        if self.connection:
            self.connection.disconnect()
            self.connection = None
            return True
        else:
            return False

    def testBrowser(self) -> None:
        self.sayHello()
        self.connectToAi(browser=True)
        print(self.connection.ask(promt = "What is the capital of France; just one word answer?", model = self.model))
        self.connection.disconnect()
        print("BrowserAI test completed.")

    def testTerminal(self) -> None:
        self.sayHello()
        self.connectToAi(browser=False, model = self.model)
        print(self.connection.ask(promt = "What is the capital of France; just one word answer?", model = self.model))
        self.connection.disconnect()
        print("TerminalAI test completed.")
    
""" if __name__ == "__main__":
    inst1 = ControllAI("Alice")
    inst1.testBrowser()
    inst2 = ControllAI("Bob")
    inst2.testTerminal()
     """