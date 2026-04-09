from src.crewOrchestration import CrewOrchestration
from src.crewAi.agents import Agents
from src.crewAi.tasks import Tasks
from src.crewAi.crews import Crews

'''
    this is the current working file; since there is no user interface yet; this is the entry point to set up agents, tasks, crews and let them run on a problem
'''


defaultModel = "qwen3-coder-30b-a3b-instruct" # default model to be used for agents if not specified otherwise; can be changed to any other model supported by crewai

if __name__ == "__main__":
    orchestration = CrewOrchestration()
    agent1 = orchestration.createAgent(model=defaultModel, role="researcher")
    task1 = orchestration.createTask(description="What is the capital of France?", agent=agent1, expected_output="The capital of France is _____.")
    crew = orchestration.createCrew(verbose=True)
    result = orchestration.runCrew()
    print(result)