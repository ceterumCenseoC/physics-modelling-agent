from dotenv import load_dotenv
import os

from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
#from crewai_tools import ArxivPaperTool #replaced with custom addition for exponential backoff
from .tools.arxivPaperWithBackoff import ArxivPaperTool # custom tool with exponential backoff for fetching arxiv papers

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class PaperFinderCrew():
    """PaperFinder crew; finds and downloads the arxiv papers."""

    agents: list[BaseAgent]
    tasks: list[Task]
    def __init__(self, outputDir: str, pdfSaveDir: str):
        self.outputDir = outputDir
        self.pdfSaveDir = pdfSaveDir

        self.verbose = True
        self.allow_delegation = False
        self.max_iter = 1

        self.temperature = 1.0
        self.top_p = 0.95
        self.max_tokens = 120_000
        self.frequency_penalty = 0
        self.presence_penalty = 0
        
        
        self.async_execution = False

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def source_gatherer(self) -> Agent:
        return Agent(
            config=self.agents_config['source_gatherer'], # type: ignore[index]
            verbose=self.verbose,
            allow_delegation=self.allow_delegation,
            max_iter=self.max_iter,
            llm=LLM(
                model = "qwen3.6-27b",
                base_url="https://chat-ai.academiccloud.de/v1",
                api_key=os.getenv("OPENAI_API_KEY"),
                temperature=self.temperature,
                top_p=self.top_p,
                max_tokens=self.max_tokens,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
            ),
            tools=[ArxivPaperTool(download_pdfs = True, save_dir = self.pdfSaveDir, use_title_as_filename = True)] # allows the agent to acces arxiv papers
        )
    
    # Learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def gathering_task(self) -> Task:
        return Task(
            config=self.tasks_config['gathering_task'], # type: ignore[index]
            markdown=True,
            async_execution=self.async_execution,
            output_file=self.outputDir + 'sources' + '.md'
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