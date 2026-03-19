from src.controllAI import ControllAI
from src.pipelineStepEnum import PipelineStepEnum
from src.responseList import ResponseList
from src.responseObj import ResponseObj

class Pipeline:
    def __init__(self, name: str):
        self.name = name
        self.referenceCollector : controllAI = None
        #self.referenceExtractor : connectAI = None # done by referenceCollector for now
        self.simpleModelConstructor : controllAI = None
        self.simpleModelChecker : controllAI = None
        self.advancedModelConstructor : controllAI = None
        self.advancedModelChecker : controllAI = None
        self.reportGenerator : controllAI = None

        self.references : str = None
        self.simpleModel : str = None
        self.advancedModel :str = None
        self.report :str  = None

#make AI requests; take their responses;
# put these responses into ra responseList