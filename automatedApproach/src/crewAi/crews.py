from crewai import Crew
from src.crewAi.agents import Agents
from src.crewAi.tasks import Tasks

class Crews:
    def __init__(self, agents : list, tasks : list, verbose : bool = True) -> None:
        self.agents : list = agents # list of Agents instances that are part of the crew
        self.tasks : list = tasks # list of Tasks instances that the crew needs to perform
        self.verbose : bool = verbose # whether to print logs during execution or not
        self.crew = Crew(
            agents=[agent.agent for agent in self.agents],
            tasks=[task.task for task in self.tasks],
            verbose=self.verbose
        )

    def run(self) -> dict:
        # this is where the logic for running the crew and coordinating the agents and tasks will go
        result = self.crew.kickoff()
        return result