from __future__ import annotations # so typechecking can recognize the class types that are defined in this file without needing to import them; allows for cleaner code and avoids circular imports
import threading
from typing import TYPE_CHECKING, Any, Optional

from attrs import inspect

from src.wrappersCrewAi.aiAccess.openAiClient import OpenAiClient
from src.wrappersCrewAi.aiAccess.embedderCustom import NoOpEmbedder
from src.wrappersCrewAi.aiAccess.noOpAnalysis import NoOpAnalysis

if TYPE_CHECKING:
    from crewai import Agent
    from crewai import Memory
    from src.wrappersCrewAi.aiAccess.lLM import LLM # uses crewAi BaseLLM, thatswhy don't import right away
    from crewai.agent.planning_config import PlanningConfig
    from crewai.llms.base_llm import BaseLLM


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
        # embedder is a custom Object that is accepted by crewai but has no real functionality for now; memory_config needed so crewai doesn't throw error when accessing memory later
        self.cache : bool = True # whether the agent should cache responses from the connected AI or not (not implemented yet)
        self.temperature : float = 0.1 # creativit of input

        # tool usage
        self.tools : list = [] # tools that the agent can use, e.g. a python interpreter, a search engine, a calculator, etc. (not implemented yet)
        self.use_tools : bool = True # whether the agent is allowed to use tools or not (not implemented yet)
        self.tool_choice : str = "auto" # how the agent should choose which tool to use, e.g. "auto", "random", "least_used", concrete list
        self.allowcodeExecution : bool = False

        # other
        self.max_input_tokens : int = 260000 # token input limit
        self.max_response_tokens : int = 260000 # token output limit
        self.system_template : str = None # custom system prompt template
        self.prompt_template : str = None # custom prompt template
        self.response_template : str = None # custom response template
        self.callbacks : list = [] # callbacks for different stages of the agents reasoning process, e.g. before/after tool use, before/after response generation, etc. (not implemented yet)   
        
        # reasoning and planning
        self.planning : bool = False # wheter the agent should have planning capabilities or not
        self.reasoning : bool = False # whether the agent should have reasoning capabilities or not; whether agent should reflect

        # init control
        self._native_initialized = False
        self._init_lock = threading.Lock()

        # native-backed attributes start as None
        self.llm : LLM = None
        self.memory : Memory = None
        self.agent : Agent = None
        self.planning_config : PlanningConfig = None # configuration for the agents planning capabilities; so default values are used
        self.delegateLlm : BaseLLM = None # optional: the plain delegate instance for internal use/tests; not required for crewAi integration, but can be useful to have direct access to the LLM interface that handles interactions with the connected AI


    def initializeNative(self) -> None:
        """Create LLM, Memory and crewai Agent exactly once, thread-safe."""

        if self._native_initialized:
            return
        
        with self._init_lock:
            if self._native_initialized:
                return
            
            # runtime imports only
            import crewai
            from crewai.agent.core import Agent
            from crewai.llms.base_llm import BaseLLM
            from src.wrappersCrewAi.aiAccess.lLM import LLM as DelegateLLM

            # create your delegate instance; the acctuall interface that handles accessing the conntected AI
            delegate = DelegateLLM(client=OpenAiClient(), model=self.model)

            # runtime adapter subclass that inherits BaseLLM
            class CrewLLM(BaseLLM):
                def __init__(self, delegate_instance: DelegateLLM):
                    # call BaseLLM.__init__ with the required model argument
                    model_name = getattr(delegate_instance, "model", None)
                    super().__init__(model=model_name)

                    # adapter state
                    self._delegate = delegate_instance
                    self.model = model_name
                    self.supports_function_calling = getattr(delegate_instance, "supports_function_calling", False)

                    # ensure _token_usage is a plain dict so BaseLLM methods work
                    token_usage = getattr(delegate_instance, "_token_usage", None)
                    if token_usage is None:
                        self._token_usage = {}
                    else:
                        # convert pydantic or other objects to dict if needed
                        self._token_usage = token_usage.dict() if hasattr(token_usage, "dict") else dict(token_usage)

                # synchronous call required by BaseLLM
                def call(self, messages, **kwargs):
                    result = self._delegate.call(messages, **kwargs)
                    # keep token usage in sync
                    self._token_usage = getattr(self._delegate, "_token_usage", {}) or {}
                    return result
            
            # instantiate adapter; handles that the LLM interface is instance of BaseLLM as expected by crewAi
            crew_llm = CrewLLM(delegate)

            # keep the plain delegate for your internal use, but set self.llm to the adapter
            self.delegateLlm = delegate      # optional: for internal calls/tests
            self.llm = crew_llm                # this is the object you pass to Agent and Memory

            self.memory = crewai.Memory(
                llm=self.llm,
                depth="shallow",
                embedder=NoOpEmbedder(),
                memory_config={"async_mode": False, "analysis": NoOpAnalysis()},
            )
            self.planning_config = crewai.agent.planning_config.PlanningConfig()

            import inspect
            from crewai.agent.core import Agent
            print(inspect.signature(Agent))

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
                callbacks = self.callbacks,
                planning_config = self.planning_config,
                reasoning = self.reasoning
            )

            # set flag only after successful creation
            self._native_initialized = True