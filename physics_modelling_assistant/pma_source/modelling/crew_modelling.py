from dotenv import load_dotenv
import os

from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from .tools.pDFReader import PDFReader # custom tool to read pdfs and extract text from them
from .tools.dimemsionalAnalysis import DimensionalAnalysis # custom tool to perform dimensional analysis

#from src.physicsmodellinghelper.embedderCustom import EmbedderCustom

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ModellerCrew():
    """modeller Crew; does everything that does not need the arxiv search"""

    agents: list[BaseAgent]
    tasks: list[Task]
    def __init__(self, outputDir: str, pdfSaveDir: str, temperature : float, top_p: float, max_tokens: int, max_iter : int, reasoning : bool, max_reasoning_attempts : int):
        self.outputDir = outputDir
        self.pdfSaveDir = pdfSaveDir

        self.verbose = True
        self.allow_delegation = False
        self.max_iter = max_iter
        self.reasoning = reasoning
        self.max_reasoning_attempts = max_reasoning_attempts

        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens
        self.frequency_penalty = 0 # parameter not used; set to default
        self.presence_penalty = 0 # parameter not used; set to default

        #self.url = "https://saia.gwdg.de/v1" # "https://chat-ai.academiccloud.de/v1"
        
        self.async_execution = False

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    
    @agent
    def information_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['information_extractor'], # type: ignore[index]
            verbose=self.verbose,
            allow_delegation=self.allow_delegation,
            max_iter=self.max_iter,
            reasoning=self.reasoning, # to allow the tool to be called on multiple formulas
            max_reasoning_attempts=self.max_reasoning_attempts, # since reasoning is disabled, this parameter is not used

            llm=LLM(
                model = "deepseek-v4-flash-0731",#"qwen3.6-27b",
                base_url=os.getenv("OPENAI_BASE_URL"),
                api_key=os.getenv("OPENAI_API_KEY"),
                temperature=self.temperature,
                top_p=self.top_p,
                max_tokens=self.max_tokens,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
            ),
            tools=[PDFReader(pdf_save_dir=self.pdfSaveDir)] # allows the agent to read pdfs
        )
    
    @agent
    def modeller(self) -> Agent:
        return Agent(
            config=self.agents_config['modeller'], # type: ignore[index]
            verbose=self.verbose,
            allow_delegation=self.allow_delegation,
            max_iter=self.max_iter,
            reasoning=self.reasoning, # to allow the tool to be called on multiple formulas
            max_reasoning_attempts=self.max_reasoning_attempts,

            llm=LLM(
                model = "deepseek-v4-flash-0731",#"deepseek-v4-flash-0731",#"glm-4.7", # scored best on logic and critpt; qwen3.5-397b-a17b
                base_url=os.getenv("OPENAI_BASE_URL"),
                api_key=os.getenv("OPENAI_API_KEY"),
                temperature= self.temperature, # allow for some creativity to perhaps correct inconsistencies in the extracted information,
                top_p=self.top_p,
                max_tokens=self.max_tokens,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
            ),
            #tools=[FileReadTool(file_path='../..runOutputs/information.md')] # for the simple modeller we currently dont see a need for tools, but we can easily add some if needed
        )

    @agent
    def unit_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['unit_checker'], # type: ignore[index]
            verbose= self.verbose,
            allow_delegation=self.allow_delegation,
            max_iter=self.max_iter,
            reasoning=self.reasoning,
            max_reasoning_attempts=self.max_reasoning_attempts,

            llm=LLM(
                model = "deepseek-v4-flash-0731",#"deepseek-v4-flash-0731",#"glm-4.7", #qwen3.5-397b-a17b
                base_url=os.getenv("OPENAI_BASE_URL"),
                api_key=os.getenv("OPENAI_API_KEY"),
                temperature= self.temperature, # to make transition between si units and not si units
                top_p=self.top_p,
                max_tokens=self.max_tokens,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
            ),
            tools=[DimensionalAnalysis()] # allows the agent to perform dimensional analysis on equations
        )
    
    @agent
    def paramter_suggester(self) -> Agent:
        return Agent(
            config=self.agents_config['paramter_suggester'], # type: ignore[index]
            verbose= self.verbose,
            allow_delegation=self.allow_delegation,
            max_iter=self.max_iter,
            reasoning=self.reasoning, # to allow the tool to be called on multiple formulas
            max_reasoning_attempts=self.max_reasoning_attempts,

            llm=LLM(
                model = "deepseek-v4-flash-0731",#"deepseek-v4-flash-0731",#"glm-4.7", #qwen3.5-397b-a17b
                base_url=os.getenv("OPENAI_BASE_URL"),
                api_key=os.getenv("OPENAI_API_KEY"),
                temperature=self.temperature,
                top_p=self.top_p,
                max_tokens=self.max_tokens,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
            )
        )
    
    @agent
    def simulation_physician(self) -> Agent:
        return Agent(
            config=self.agents_config['simulation_physician'], # type: ignore[index]
            verbose=self.verbose,
            allow_delegation=self.allow_delegation,
            max_iter=self.max_iter,
            reasoning=self.reasoning, # to allow the tool to be called on multiple formulas
            max_reasoning_attempts=self.max_reasoning_attempts,

            llm=LLM(
                model = "deepseek-v4-flash-0731",#"deepseek-v4-flash-0731",#"glm-4.7", #qwen3.5-397b-a17b
                base_url=os.getenv("OPENAI_BASE_URL"),
                api_key=os.getenv("OPENAI_API_KEY"),
                temperature=self.temperature, # just coding
                top_p=self.top_p,
                max_tokens=self.max_tokens,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
            )
        )
    
    
    @agent
    def simulation_correcter(self) -> Agent:
        return Agent(
            config=self.agents_config['simulation_correcter'], # type: ignore[index]
            verbose=self.verbose,
            allow_delegation=self.allow_delegation,
            max_iter=self.max_iter,
            reasoning=self.reasoning,
            max_reasoning_attempts=self.max_reasoning_attempts,

            llm=LLM(
                model = "deepseek-v4-flash-0731",#"deepseek-v4-flash-0731",#"glm-4.7", # scored best on logic and critpt; qwen3.5-397b-a17b
                base_url=os.getenv("OPENAI_BASE_URL"),
                api_key=os.getenv("OPENAI_API_KEY"),
                temperature=self.temperature,
                top_p=self.top_p,
                max_tokens=self.max_tokens,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
            ),
            allow_code_execution=True
            #tools = [CodeInterpreterTool()]
        )

    @agent
    def final_outputer(self) -> Agent:
        return Agent(
            config=self.agents_config['final_outputer'], # type: ignore[index]
            verbose=self.verbose,
            allow_delegation=self.allow_delegation,
            max_iter=self.max_iter,
            reasoning=self.reasoning,
            max_reasoning_attempts=self.max_reasoning_attempts,

            llm=LLM(
                model = "deepseek-v4-flash-0731",#"deepseek-v4-flash-0731",#"glm-4.7", # scored best on logic and critpt; qwen3.5-397b-a17b
                base_url=os.getenv("OPENAI_BASE_URL"), # default to the new URL if BASE_URL is not set
                api_key=os.getenv("OPENAI_API_KEY"),
                temperature=self.temperature,
                top_p=self.top_p,
                max_tokens=self.max_tokens,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
            )
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    
    @task
    def extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['extraction_task'], # type: ignore[index]
            markdown=True,
            async_execution=self.async_execution,
            output_file=self.outputDir + 'information' + '.md'
        )
    
    @task
    def modelling_task(self) -> Task:
        return Task(
            config=self.tasks_config['modelling_task'], # type: ignore[index]
            markdown=True,
            async_execution=self.async_execution,
            output_file=self.outputDir + 'model' + '.md'
        )
    
    @task
    def unit_checking_task(self) -> Task:
        return Task(
            config=self.tasks_config['unit_checking_task'], # type: ignore[index]
            markdown=True,
            async_execution=self.async_execution,
            output_file=self.outputDir + 'unit_check' + '.md'
        )
    
    @task
    def parameter_suggestion_task(self) -> Task:
        return Task(
            config=self.tasks_config['parameter_suggestion_task'], # type: ignore[index]
            markdown=True,
            async_execution=self.async_execution,
            output_file=self.outputDir + 'parameter_suggestion' + '.md'
        )
        
    @task
    def physician_simulation_task(self) -> Task:
        return Task(
            config=self.tasks_config['physician_simulation_task'], # type: ignore[index]
            markdown=False,
            async_execution=self.async_execution,
            output_file=self.outputDir + 'simulation_physician' + '.py'
        )

    @task
    def simulation_correction_task(self) -> Task:
        return Task(
            config=self.tasks_config['simulation_correction_task'], # type: ignore[index]
            markdown=False,
            async_execution=self.async_execution,
            output_file=self.outputDir + 'simulation_correction' + '.py'
        )
    
    @task
    def final_output_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_output_task'], # type: ignore[index]
            markdown=False,
            async_execution=self.async_execution,
            output_file=self.outputDir + 'final_output' + '.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Physicsmodellinghelper crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential, # for simplicity
            verbose=self.verbose,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )