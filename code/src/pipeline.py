import connectAI
import pipelineStepEnum
import responseList
import responseObj

class Pipeline:
    def __init__(self, name: str):
        self.name = name
        self.referenceCollector : connectAI = None
        #self.referenceExtractor : connectAI = None # done by referenceCollector for now
        self.simpleModelConstructor : connectAI = None
        self.simpleModelChecker : connectAI = None
        self.advancedModelConstructor : connectAI = None
        self.advancedModelChecker : connectAI = None
        self.reportGenerator : connectAI = None

        self.references : str = None
        self.simpleModel : str = None
        self.advancedModel :str = None
        self.report :str  = None

#make AI requests; take their responses;
# put these responses into ra responseList