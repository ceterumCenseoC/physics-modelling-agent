from src.wrappersCrewAi.agents import Agents
from src.wrappersCrewAi.tasks import Tasks

class Crews:
    '''wrapper class for the Crew class from crewai; wraps the specification in parameters'''
    def __init__(self, agents : list, tasks : list, verbose : bool = True) -> None:
        self.agents : list = agents # list of Agents instances that are part of the crew
        self.tasks : list = tasks # list of Tasks instances that the crew needs to perform
        self.verbose : bool = verbose # whether to print logs during execution or not
        from crewai import Crew
        self.crew = Crew( # set up the Crew Object from crewai based on the parameters
            agents=[agent.agent for agent in self.agents],
            tasks=[task.task for task in self.tasks],
            verbose=self.verbose
        )

    def run(self) -> dict:
        # starts the working process of the crew and returns the final result
        result = self.crew.kickoff()
        return result
    
    def run(self, argumentsDict : dict) -> dict:
        # starts the working process of the crew and returns the final result
        result = self.crew.kickoff(argumentsDict)
        return result