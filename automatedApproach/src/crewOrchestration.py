from src.wrappersCrewAi.agents import Agents
from src.wrappersCrewAi.tasks import Tasks
from src.wrappersCrewAi.crews import Crews

class CrewOrchestration:
    '''this class is used to create crews, agents and tasks; it is seperated from the Crews class to keep the structrure of crewAi'''
    '''in the future, multiple crews could be created and orchestrated thogether with this class'''
    def __init__(self) -> None:
        self.agents : list = [] # list of Agents instances that are part of the crew
        self.tasks : list = [] # list of Tasks instances that the crew needs to perform
        self.crew : Crews = None # instance of the Crews class that will be created based on the specified agents and tasks
    
    def addAgent(self, agent : Agents) -> None:
        self.agents.append(agent)
        print (f"Agent has: {agent.planning} planning and {agent.reasoning} reasoning capabilities. {agent.planning_config}; thats iot.")
    
    def addTask(self, task : Tasks) -> None:
        self.tasks.append(task)

    def addCrew(self, crew : Crews) -> None:
        self.crew = crew

    def createAgent(self, model : str, role : str) -> Agents:
        # creates the agent and includes it in the list of agents for the crew
        agent = Agents(model=model, role=role)
        agent.initializeNative() # initialize the native-backed attributes of the agent (LLM, Memory, crewai Agent)
        self.addAgent(agent)
        return agent
    
    def createTask(self, description : str, agent : Agents, expected_output : str) -> Tasks:
        # creates the task and includes it in the list of tasks for the crew
        task = Tasks(description=description, agent=agent, expected_output=expected_output)
        self.addTask(task)
        return task
    
    def createCrew(self, verbose : bool = True) -> Crews:
        # creates the crew based on the agents and tasks that have been specified and included
        crew = Crews(agents=self.agents, tasks=self.tasks, verbose=verbose)
        self.addCrew(crew)
        return crew
    
    def runCrew(self) -> dict:
        # executes the crews run method which starts the crewAi process
        if self.crew is None:
            raise ValueError("Crew has not been created yet. Please create a crew before running it.")
        result = self.crew.run() # starts the process
        return result