from src.pipelineStepEnum import PipelineStepEnum
from typing import Any

class ResponseObj:
    '''Class to represent a response object, which can be used to store a response and its associated query and the following ResponseObj'''
    def __init__(self, query: str) -> None:
        self.functionOfStep : PipelineStepEnum = None
        self.query : str = dict[str: Any]
        self.aiModel : str = None
        self.response : str = None
        self.responseId : str = None
        self.nextPipelineStep : ResponseObj = None
        """self.tryOfStep : int = None # to keep track of how many times a step has been tried, in case of failure, to avoid infinite loops"""
    
    def setfunctionOfStep(self, pipelineStep : PipelineStepEnum) -> bool:
        self.pipelineStep = pipelineStep
        return True

    def setAiModel(self, aiModel : str) -> bool:
        self.aiModel = aiModel
        return True

    def setQuery(self, query : str) -> bool:
        self.query = query
        return True
    
    def setResponse(self, response : str) -> bool:
        self.response = response
        return True

    def setResponseId(self, responseId : str) -> bool:
        self.responseId = responseId
        return True

    def setNextPipelineStep(self, nextPipelineStep : 'ResponseObj') -> bool:
        self.nextPipelineStep = nextPipelineStep
        return True
    
    """ def setTryOfStep(self, tryOfStep : int) -> bool:
        self.tryOfStep = tryOfStep
        return True """
    
    def getFunctionObStep(self) -> 'PipelineStepEnum':
        return self.pipelineStep

    def getAiModel(self) -> str:
        return self.aiModel

    def getQuery(self) -> str:
        return self.query

    def getResponse(self) -> str:
        return self.response

    def getResponseId(self) -> str:
        return self.responseId
    
    def getNextPipelineStep(self) -> 'ResponseObj':
        return self.nextPipelineStep
    
    """ def getTryOfStep(self) -> int:
        return self.tryOfStep """
    
    def __str__(self) -> str:
        string = f"Pipeline Step: {self.pipelineStep.value}\nAI Model: {self.aiModel}\nQuery: {self.query}\nResponse: {self.response}\n"
        return string