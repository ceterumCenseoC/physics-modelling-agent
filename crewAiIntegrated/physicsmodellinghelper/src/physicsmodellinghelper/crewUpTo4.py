from dotenv import load_dotenv
import os

from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import ScrapeWebsiteTool, ArxivPaperTool

#from crewai_tools import WebsiteSearchTool
#from physicsmodellinghelper.embedderCustom import EmbedderCustom

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Physicsmodellinghelper():
    """Physicsmodellinghelper crew"""

    agents: list[BaseAgent]
    tasks: list[Task]
    runNr : int = 4 # this number is added to the output files to distinguish between runs

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
                #type="chat-completions"
            ),
            tools=[ArxivPaperTool(download_pdf=True, output_dir='./arxiv_papers', use_title_as_filename=True)] # allows the agent to download PDFs
        )   # download doesn't work, i suppose an internet provider issue
        """ ScrapeWebsiteTool(website_url='https://www.nature.com/articles/s41567-023-02121-4'),
                   ScrapeWebsiteTool(website_url='https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.3.013275'),
                   ScrapeWebsiteTool(website_url='https://www.nature.com/articles/s43246-025-00952-7'),
                   #ScrapeWebsiteTool(website_url='https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.134.166401'),
                   ScrapeWebsiteTool(website_url='https://arxiv.org/html/2604.13948v1'), """ #previous websites

    
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
                #type="chat-completions"
            ),
            tools=[ArxivPaperTool(download_pdf=True, output_dir='./arxiv_papers', use_title_as_filename=True)] # allows the agent to download PDFs
        )
    
    @agent
    def simple_modeller(self) -> Agent:
        return Agent(
            config=self.agents_config['simple_modeller'], # type: ignore[index]
            verbose=True,
            temperature=0.2,
            llm=LLM(
                model = "deepseek-r1-distill-llama-70b",
                base_url="https://chat-ai.academiccloud.de/v1",
                api_key=os.getenv("OPENAI_API_KEY"),
                #type="chat-completions"
            )
        )
    
    @agent
    def model_simulator(self) -> Agent:
        return Agent(
            config=self.agents_config['model_simulator'], # type: ignore[index]
            verbose=True,
            temperature=0.1,
            llm=LLM(
                model = "devstral-2-123b-instruct-2512",
                base_url="https://chat-ai.academiccloud.de/v1",
                api_key=os.getenv("OPENAI_API_KEY"),
                #type="chat-completions"
            )
        )
    
    @agent
    def checker(self) -> Agent:
        return Agent(
            config=self.agents_config['checker'], # type: ignore[index]
            verbose=True,
            temperature=0.0,
            llm=LLM(
                model = "qwen3.5-122b-a10b", #MODEL NEEDS TO SUPPORT AUTO TOOL CALLING; strong logic model for comparision: we want an understading of the output; OR strong overall model for better text parsing and comparisions???
                base_url="https://chat-ai.academiccloud.de/v1",
                api_key=os.getenv("OPENAI_API_KEY"),
                #type="chat-completions"
            ),
            tools=[ArxivPaperTool(downlaod_pdf=True, output_dir='./arxiv_papers', use_title_as_filename=True)]
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def gathering_task(self) -> Task:
        return Task(
            config=self.tasks_config['gathering_task'], # type: ignore[index]
            markdown=True,
            output_file='runOutputs/sources'+str(self.runNr)+'.md'
        )
    
    @task
    def extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['extraction_task'], # type: ignore[index]
            markdown=True,
            output_file='runOutputs/information'+str(self.runNr)+'.md'
        )
    
    @task
    def simple_modelling_task(self) -> Task:
        return Task(
            config=self.tasks_config['simple_modelling_task'], # type: ignore[index]
            markdown=True,
            output_file='runOutputs/simple_model'+str(self.runNr)+'.md'
        )
    
    @task
    def simulation_task(self) -> Task:
        return Task(
            config=self.tasks_config['simulation_task'], # type: ignore[index]
            markdown=False,
            output_file='runOutputs/simulation_results'+str(self.runNr)+'.py'
        )
    
    @task
    def checking_task(self) -> Task:
        return Task(
            config=self.tasks_config['checking_task'], # type: ignore[index]
            markdown=True,
            output_file='runOutputs/checking_results'+str(self.runNr)+'.md'
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