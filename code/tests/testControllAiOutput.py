from src.aiAccessBrowser import AiAccessBrowser
from src.aiAccessTerminal import AiAccessTerminal
from src.controllAI import ControllAI
from src.aiAccessInterface import AiAccessInterface
from src.pipelineStepEnum import PipelineStepEnum


# This is for cmd line testing; manly when you don't know the expected output yet
ai = ControllAI(name="TestAI", modelsGeneralPurpose="General purpose for testing")
print("stage1")
ai.connectToAi(browser=False)
print("stage2")

terminalAi = AiAccessTerminal()
terminalAi.listModels()
print(ai.listModels()[0])
print("stage3")
