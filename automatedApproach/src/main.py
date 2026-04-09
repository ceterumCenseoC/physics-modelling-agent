from src.crewOrchestration import CrewOrchestration
from src.wrappersCrewAi.agents import Agents
from src.wrappersCrewAi.tasks import Tasks
from src.wrappersCrewAi.crews import Crews

'''
    this is the current working file; since there is no user interface yet; this is the entry point to set up agents, tasks, crews and let them run on a problem
'''


defaultModel = "qwen3-coder-30b-a3b-instruct" # default model to be used for agents if not specified otherwise; can be changed to any other model supported by crewai

if __name__ == "__main__":

    orchestration = CrewOrchestration()
    agent1 = orchestration.createAgent(model=defaultModel, role="researcher")
    task1 = orchestration.createTask(description="What is the capital of France?", agent=agent1, expected_output="The capital of France is ___.")
    crew = orchestration.createCrew(verbose=True)
    result = None
    #result = orchestration.runCrew()
    import sys, traceback

    try:
        result = orchestration.runCrew()   # or self.crew.kickoff()
    except Exception:
        traceback.print_exc()
        tb = sys.exc_info()[2]
        while tb.tb_next:
            tb = tb.tb_next
        frame = tb.tb_frame
        print("\n--- Exception frame info ---")
        print("File:", frame.f_code.co_filename)
        print("Function:", frame.f_code.co_name)
        print("Line:", tb.tb_lineno)
        print("\nLocal variables in that frame (name: type = repr):")
        for k, v in frame.f_locals.items():
            try:
                print(f"  {k}: {type(v).__name__} = {repr(v)[:400]}")
            except Exception:
                print(f"  {k}: {type(v).__name__} = <repr failed>")
        raise
    print(result)