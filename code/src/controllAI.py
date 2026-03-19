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

    def listModels(self) -> list:
        '''only works for terminal'''        
        if self.connection is None:
            self.connectToAi()
        return self.connection.listModels()
    
    def setModel(self, model : str) -> None:
        '''sets the model that will be used for requests; checks if the specified model is actually in the connected AI, otherwise raises an error'''
        if self.connection is None:
            self.connectToAi(browser=False) # makes sure, a Model exists

        if model not in self.connection.listModels():
            raise ValueError(f"The specified model '{model}' is not available in the connected AI.")
        
        self.model = model

    def setModelToDefault(self) -> None:
        '''sets the model to a default value, which is the first model in the list of available models from the connected AI'''
        if self.connection is None:
            self.connectToAi(browser=False) # makes sure, a Model exists

        self.model = self.connection.listModels()[0]

    def checkConnection(self, model : str = None) -> bool:
        '''checks wheter a test prompt works and sets a default model'''
        if self.connection is None:
            self.connectToAi(browser=False) # makes sure, a Model exists
        if model is None:
            if self.model is None:
                self.setModelToDefault() # sets the model attribute to a default value, which is the first model in the list of available models from the connected AI
            return self.connection.connect(self.model)
        
        # check wheter the specified model is actually in the connected AI, otherwise raise an error
        if model not in self.connection.listModels():
            raise ValueError(f"The specified model '{model}' is not available in the connected AI.")

        return self.connection.connect(model)
    
    def ask(self, promt : str, questionTheModelShouldWorkOn : str, previousModelsWork : str, modelsGeneralPurpose : str = None, model : str = None, reasoningEffort : str = None) -> tuple[dict[str, Any], str]:
        if self.connection is None:
            self.connectToAi(browser=False) # makes sure, a Model exists

        if modelsGeneralPurpose is None:
            modelsGeneralPurpose = self.generalPurpose # must be set by default

        if model is None: # when no model is specified
            if self.model is None: #rely on the model attribut, but if this is also None
                self.setModelToDefault() # perform checkConnection(), which sets the model attribute to a default value
            model = self.model
        
        # check wheter the specified model is actually in the connected AI, otherwise raise an error
        if model not in self.connection.listModels():
            raise ValueError(f"The specified model '{model}' is not available in the connected AI.")

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
