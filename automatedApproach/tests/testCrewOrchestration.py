from src.crewOrchestration import CrewOrchestration

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