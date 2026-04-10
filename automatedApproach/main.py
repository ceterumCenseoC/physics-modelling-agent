from src.crewOrchestration import CrewOrchestration
from src.wrappersCrewAi.agents import Agents
from src.wrappersCrewAi.tasks import Tasks
from src.wrappersCrewAi.crews import Crews
from src.wrappersCrewAi.aiAccess.openAiClient import OpenAiClient

defaultModel = "qwen3-coder-30b-a3b-instruct" # default model to be used for agents if not specified otherwise; can be changed to any other model supported by crewai

if __name__ == "__main__":

    saia = OpenAiClient()
    print(saia.listModels()) # prints the list of available models from the AI service 

    orchestration = CrewOrchestration()
    agent1 : Agents = orchestration.createAgent(model=defaultModel, name = "information_gatherer", role="researcher")
    task1 : Tasks = orchestration.createTask(name = "Information Gathering", description="What is the capital of France?", agent=agent1, expected_output="The capital of France is ___.")
    crew : Crews = orchestration.createCrew(verbose=True)
    result = orchestration.runCrew()
    print(result.raw)