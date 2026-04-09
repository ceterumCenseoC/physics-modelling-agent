import threading
import crewai
from crewai import Agent
from crewai import Memory
from src.wrappersCrewAi.aiAccess.lLM import LLM
from src.wrappersCrewAi.aiAccess.openAiClient import OpenAiClient
from src.wrappersCrewAi.aiAccess.embedderCustom import NoOpEmbedder

class Agents:
    '''wrapper class around the Agent class from crewai; used for easier storage and management of the LLM used'''
    def __init__(self, model : str, role : str) -> None:
        self.role : str = role # agents identity, e.g. "Researcher", "Writer", "Analyst", etc.
        self.goal : str = "efficient answers" # long term goal of the agent
        self.backstory : str = "well educated person with a strong background in the field" # context and backround info
        self.model : str = model # model to use for the agent, e.g. "gpt-4o", "gpt-3.5-turbo", etc.
        #self.llm : LLM = LLM(client = OpenAiClient(), model = self.model) # instance of the LLM class, which serves as the interface to the connected AI
        self.verbose : bool = True # whether to print logs during execution or not

        # behavioral/execution parameters
        self.max_iter : int = 20 # maximum reasoing steps that aget can take
        self.max_rpm : int = 20000 # max requests per minute that the agent can make to the connected AI
        self.allow_delegation : bool = True # whether the agent is allowed to delegate tasks to other agents or not (not implemented yet)
        #self.memory : Memory = Memory(llm=self.llm, depth="shallow", embedder=NoOpEmbedder(), memory_config={"async_mode": False, "analysis": False}) # meomory object for remembering previous interactions and information; SHALLOW memory because for deep memory custom embedding modell would be needed
        # embedder is a custom Object that is accepted by crewai but has no real functionality for now; memory_config needed so crewai doesn't throw error when accessing memory later
        #self.memory : bool = False # whether the agent should have memory of previous interactions or not (not implemented yet)
        self.cache : bool = True # whether the agent should cache responses from the connected AI or not (not implemented yet)
        self.temperature : float = 0.1 # creativit of input

        # tool usage
        self.tools : list = [] # tools that the agent can use, e.g. a python interpreter, a search engine, a calculator, etc. (not implemented yet)
        self.use_tools : bool = True # whether the agent is allowed to use tools or not (not implemented yet)
        self.tool_choice : str = "auto" # how the agent should choose which tool to use, e.g. "auto", "random", "least_used", concrete list

        # other
        self.max_input_tokens : int = 260000 # token input limit
        self.max_response_tokens : int = 260000 # token output limit
        self.system_template : str = None # custom system prompt template
        self.prompt_template : str = None # custom prompt template
        self.response_template : str = None # custom response template
        self.callbacks : list = [] # callbacks for different stages of the agents reasoning process, e.g. before/after tool use, before/after response generation, etc. (not implemented yet)   
        
        # reasoning and planning
        self.planning_config : crewai.agent.planning_config.PlanningConfig = crewai.agent.planning_config.PlanningConfig() # configuration for the agents planning capabilities; not implemented yet, so default values are used
        self.planning : bool = True # wheter the agent should have planning capabilities or not
        self.reasoning : bool = True # whether the agent should have reasoning capabilities or not; whether agent should reflect

        # native-backed attributes start as None
        self.llm = None
        self.memory = None
        self.agent = None

        # init control
        self._native_initialized = False
        self._init_lock = threading.Lock()
    
    def initializeNative(self) -> None:
        """Create LLM, Memory and crewai Agent exactly once, thread-safe."""

        if self._native_initialized:
            return
        
        with self._init_lock:
            if self._native_initialized:
                return
            
            # Initialize native-backed attributes
            self.llm = LLM(client = OpenAiClient(), model = self.model)
            self.memory = Memory(llm=self.llm, depth="shallow", embedder=NoOpEmbedder(), memory_config={"async_mode": False, "analysis": False})

            self.agent = Agent( #setupt the agent with the specified parameters
                role=self.role,
                llm = self.llm, #to access the lLM interface that can handle all interactions with the connected AI; allows access to any model at access
                goal=self.goal,
                backstory=self.backstory,
                model=self.model,
                verbose=self.verbose,
                max_iter = self.max_iter,
                max_rpm = self.max_rpm,
                allow_delegation = self.allow_delegation,
                memory = self.memory,
                cache = self.cache,
                temperature = self.temperature,
                tools = self.tools,
                use_tools = self.use_tools,
                tool_choice = self.tool_choice,
                max_input_tokens = self.max_input_tokens,
                max_response_tokens = self.max_response_tokens,
                system_template = self.system_template,
                prompt_template = self.prompt_template,
                response_template = self.response_template,
                callbacks = self.callbacks
            )

            # set flag only after successful creation
            self._native_initialized = True