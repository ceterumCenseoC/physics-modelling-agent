from crewai import Task
from src.wrappersCrewAi.agents import Agents

class Tasks:
    '''wrapper class for the Task class from crewai; wraps the specification in parameters; can be expanded to hold specifications that override the used agent's defualt behaviour'''
    def __init__(self, description : str, agent : Agents, expected_output : str) -> None:
        self.description : str = description # description of the task to be performed by the assigned agent
        self.agent : Agents = agent # agent that is assigned to perform the task
        self.expected_output : str = expected_output # expected output format or content of the task, e.g. "A structured summary with citations.", "A list of relevant papers with links.", "A concise answer in one sentence.", etc.
        #other paramters can be specified here that override the default behaviour of the assigned agent for this specific task; not done yet for simplicity
        self.task = Task(
            description=self.description,
            agent=self.agent.agent, #needs to be agent.agent because the Agents class is a wrapper around the Agent class from crewai, which is what the Task class expects
            expected_output=self.expected_output
        )