from src.crewOrchestration import CrewOrchestration

#monkey-patch
from crewai.agent.core import Agent

# Disable deprecated attributes so CrewAI never checks them
Agent.allow_code_execution = False
Agent.reasoning = False
Agent.planning_config = True  # anything non-None avoids the warning


class TestCrewOrchestration:
    def test_add_agent(self):
        orchestration = CrewOrchestration()
        agent = orchestration.createAgent(model="qwen3-coder-30b-a3b-instruct", role="researcher")
        assert len(orchestration.agents) == 1
        assert orchestration.agents[0] == agent

    def test_add_task(self):
        orchestration = CrewOrchestration()
        agent = orchestration.createAgent(model="qwen3-coder-30b-a3b-instruct", role="researcher")
        task = orchestration.createTask(description="What is the capital of France?", agent=agent, expected_output="The capital of France is _____.")
        assert len(orchestration.tasks) == 1
        assert orchestration.tasks[0] == task

    def test_create_crew(self):
        orchestration = CrewOrchestration()
        agent = orchestration.createAgent(model="qwen3-coder-30b-a3b-instruct", role="researcher")
        task = orchestration.createTask(description="What is the capital of France?", agent=agent, expected_output="The capital of France is _____.")
        crew = orchestration.createCrew(verbose=True)
        assert orchestration.crew == crew

    """ def test_run_crew(self):
        orchestration = CrewOrchestration()
        agent1 = orchestration.createAgent(model="qwen3-coder-30b-a3b-instruct", role="researcher")
        task1 = orchestration.createTask(description="What is the capital of France? One Word Answer:", agent=agent1, expected_output="The capital of France is _____.")
        crew = orchestration.createCrew(verbose=True)
        result = orchestration.runCrew()
        assert result == "The capital of France is Paris." """