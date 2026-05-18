from dotenv import load_dotenv
import os

from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import ArxivPaperTool
from physicsmodellinghelperCustomSim.tools.arxivSearch import ArxivDownloader # custom tool to download arxiv papers based on search results
from physicsmodellinghelperCustomSim.tools.pDFReader import PDFReader # custom tool to read pdfs and extract text from them

#from src.physicsmodellinghelper.embedderCustom import EmbedderCustom

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Physicsmodellinghelper():
    """Physicsmodellinghelper crew"""

    agents: list[BaseAgent]
    tasks: list[Task]
    def __init__(self, outputNr: int, outputDir: str):
        self.outputNr : int = outputNr
        self.outputDir = outputDir + f"runNr_{self.outputNr}/"

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def source_gatherer(self) -> Agent:
        return Agent(
            config=self.agents_config['source_gatherer'], # type: ignore[index]
            verbose=True,
            temperature=0.0,
            llm=LLM(
                model = "qwen3.5-122b-a10b",
                base_url="https://chat-ai.academiccloud.de/v1",
                api_key=os.getenv("OPENAI_API_KEY"),
                #reasoning="fast", # not supported for qwen
            ),
            tools=[ArxivPaperTool()] # allows the agent to acces arxiv papers
        )
    
    @agent
    def paper_downloader(self) -> Agent:
        return Agent(
            config=self.agents_config['paper_downloader'], # type: ignore[index]
            verbose=True,
            temperature=0.0,
            llm=LLM(
                model = "qwen3.5-122b-a10b",
                base_url="https://chat-ai.academiccloud.de/v1",
                api_key=os.getenv("OPENAI_API_KEY"),
                #type="chat-completions"
            ),
            tools=[ArxivDownloader(run_identifier=str(self.outputNr))]# allows the agent to download PDFs
        )

    @agent
    def information_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['information_extractor'], # type: ignore[index]
            verbose=True,
            temperature=0.0,
            llm=LLM(
                model = "qwen3.5-122b-a10b",
                base_url="https://chat-ai.academiccloud.de/v1",
                api_key=os.getenv("OPENAI_API_KEY"),
                max_tokens=8000,
                #type="chat-completions"
            ),
            tools=[PDFReader(run_identifier=str(self.outputNr))] # allows the agent to read pdfs
        )
    
    @agent
    def simple_modeller(self) -> Agent:
        return Agent(
            config=self.agents_config['simple_modeller'], # type: ignore[index]
            verbose=True,
            temperature=0.0,
            llm=LLM(
                model = "deepseek-r1-distill-llama-70b",
                base_url="https://chat-ai.academiccloud.de/v1",
                api_key=os.getenv("OPENAI_API_KEY"),
                #reasoning="deep", # for better reasoning capabilities; should be supported for deepseek
                #type="chat-completions"
            ),
            #tools=[FileReadTool(file_path='../..runOutputs/information.md')] # for the simple modeller we currently dont see a need for tools, but we can easily add some if needed
        )

    @agent
    def simulation_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['simulation_planner'], # type: ignore[index]
            verbose=True,
            temperature=0.0,
            llm=LLM(
                model = "deepseek-r1-distill-llama-70b", # needed because we want to read pdf's
                base_url="https://chat-ai.academiccloud.de/v1",
                api_key=os.getenv("OPENAI_API_KEY"),
            )
        )
    
    @agent
    def simulation_implementer(self) -> Agent:
        return Agent(
            config=self.agents_config['simulation_implementer'], # type: ignore[index]
            verbose=True,
            temperature=0.0,
            llm=LLM(
                model = "devstral-2-123b-instruct-2512",
                base_url="https://chat-ai.academiccloud.de/v1",
                api_key=os.getenv("OPENAI_API_KEY"),
                #type="chat-completions"
            ),
            allow_code_execution=True
            #tools = [CodeInterpreterTool()]
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def gathering_task(self) -> Task:
        return Task(
            config=self.tasks_config['gathering_task'], # type: ignore[index]
            markdown=True,
            output_file=self.outputDir + 'sources' + str(self.outputNr) + '.md'
        )
    
    @task
    def downloading_task(self) -> Task:
        return Task(
            config=self.tasks_config['downloading_task'], # type: ignore[index]
            markdown=True,
            output_file=self.outputDir + 'downloading_report' + str(self.outputNr) + '.md'
        )
    
    @task
    def extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['extraction_task'], # type: ignore[index]
            markdown=True,
            output_file=self.outputDir + 'information' + str(self.outputNr) + '.md'
        )
    
    @task
    def simple_modelling_task(self) -> Task:
        return Task(
            config=self.tasks_config['simple_modelling_task'], # type: ignore[index]
            markdown=True,
            output_file=self.outputDir + 'simple_model' + str(self.outputNr) + '.md'
        )
    
    @task
    def simulation_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['simulation_planning_task'], # type: ignore[index]
            markdown=True,
            output_file=self.outputDir + 'simulation_plan' + str(self.outputNr) + '.md'
        )

    @task
    def simulation_task(self) -> Task:
        return Task(
            config=self.tasks_config['simulation_task'], # type: ignore[index]
            markdown=False,
            output_file=self.outputDir + 'simulation_results' + str(self.outputNr) + '.py'
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
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )