from src.crewAi.agents import Agents
from src.crewAi.tasks import Tasks
from src.crewAi.crews import Crews

class CrewOrchestration:
    def __init__(self) -> None:
        self.agents : list = [] # list of Agents instances that are part of the crew
        self.tasks : list = [] # list of Tasks instances that the crew needs to perform
        self.crew : Crews = None # instance of the Crews class that will be created based on the specified agents and tasks
    
    def addAgent(self, agent : Agents) -> None:
        self.agents.append(agent)
    
    def addTask(self, task : Tasks) -> None:
        self.tasks.append(task)

    def addCrew(self, crew : Crews) -> None:
        self.crew = crew

    def createAgent(self, model : str, role : str) -> Agents:
        agent = Agents(model=model, role=role)
        self.addAgent(agent)
        return agent
    
    def createTask(self, description : str, agent : Agents, expected_output : str) -> Tasks:
        task = Tasks(description=description, agent=agent, expected_output=expected_output)
        self.addTask(task)
        return task
    
    def createCrew(self, verbose : bool = True) -> Crews:
        crew = Crews(agents=self.agents, tasks=self.tasks, verbose=verbose)
        self.addCrew(crew)
        return crew
    
    def runCrew(self) -> dict:
        if self.crew is None:
            raise ValueError("Crew has not been created yet. Please create a crew before running it.")
        result = self.crew.run()
        return result