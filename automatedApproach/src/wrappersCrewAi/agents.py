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
        self.max_rpm : int = 20000 # max requests per minute that the agent can make to the connected AI
        self.cache : bool = True # whether the agent should cache responses from the connected AI or not (not implemented yet)
        self.temperature : float = 0.1 # creativit of input

        # tool usage
        self.tools : list = [] # tools that the agent can use, e.g. a python interpreter, a search engine, a calculator, etc. (not implemented yet)
        
        # other
        self.max_input_tokens : int = 260000 # token input limit
        self.max_response_tokens : int = 260000 # token output limit
        self.system_template : str = None # custom system prompt template
        self.prompt_template : str = None # custom prompt template
        self.response_template : str = None # custom response template
        self.callbacks : list = [] # callbacks for different stages of the agents reasoning process, e.g. before/after tool use, before/after response generation, etc. (not implemented yet)   
       
        # internal state
        self._native_initialized : bool = False
        self._init_lock : threading.Lock = threading.Lock() # lock to ensure thread-safe initialization of native-backed attributes

        # native-backed attributes start as None
        self.llm : LLM = None
        self.memory : Memory = None
        self.agent : Agent = None
        self.delegateLlm : BaseLLM = None # optional: the plain delegate instance for internal use/tests; not required for crewAi integration, but can be useful to have direct access to the LLM interface that handles interactions with the connected AI
        # reasoning and planning
        self.planning_config : PlanningConfig = None # wheter the agent should have planning capabilities or not

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
            from crewai import PlanningConfig
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


            self.planning_config = PlanningConfig(
                max_depth=7,
                max_branches=7,
                strategy="reactive"
            )

            import traceback

            try:
                self.agent = Agent(
                    role=self.role,
                    llm=self.llm,
                    goal=self.goal,
                    backstory=self.backstory,
                    model=self.model,
                    verbose=self.verbose,
                    max_rpm=self.max_rpm,
                    memory=self.memory,
                    cache=self.cache,
                    temperature=self.temperature,
                    tools=self.tools,
                    max_input_tokens=self.max_input_tokens,
                    max_response_tokens=self.max_response_tokens,
                    callbacks=self.callbacks,

                    # Modern planning system
                    #planning=False,                 # disable old planning engine
                    #reasoning=False,                # disable old reasoning engine
                    #planning_config=self.planning_config
                )

                #planning_config=self.planning_config # this causes reasoning to fail

            except Exception:
                traceback.print_exc()
                raise

            # set flag only after successful creation
            self._native_initialized = True