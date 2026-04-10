from src.crewOrchestration import CrewOrchestration
from src.wrappersCrewAi.agents import Agents
from src.wrappersCrewAi.tasks import Tasks
from src.wrappersCrewAi.crews import Crews
from src.wrappersCrewAi.aiAccess.openAiClient import OpenAiClient

if __name__ == "__main__":

    """ saia = OpenAiClient()
    print(saia.listModels()) # prints the list of available models from the AI service """ 
    
    orchestration = CrewOrchestration()

    agent1 : Agents = orchestration.createAgent(model="qwen3.5-122b-a10b", name = "information gatherer", role="gather information about the {problem}")
    agent1.goal = "find 2-5 relevant pieces of information about the {problem} that will help solving it. Preferably scientific papers or books"
    agent1.backstory = "well educated scientist knowing the common approaches to most physics problems, but not an expert in the specific {problem} at hand. Does the groundwork so other agents can shine."
    agent1.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the information gatherer agent, because it needs to provide a detailed description of the relevant information that can be quite long, especially if the problem is complex; without setting this, the agent might not be able to provide a complete description of the relevant information, which would make it harder for the other agents to work with it and also limit the performance of the whole crew in solving the problem.

    task1 : Tasks = orchestration.createTask(name = "Information Gathering", 
                                             description="Find information about the scientific {problem} at hand. Filter for relevance and quality.", agent=agent1, 
                                             expected_output="A descriptio of the relevant approaches (and information) to the {problem}, preferably with links to scientific papers or books. The description should be concise but informative enough for other agents to work with it.")
    

    agent2 : Agents = orchestration.createAgent(model="deepseek-r1-distill-llama-70b", name = "simple model maker", role="make simple model for the {problem}")
    agent2.goal = "propose a simple model that is somewhat similar to the real {problem} but simpler to solve, based on the information provided by the information gatherer. The model should have already been solved in the literature, so the agent can find the solution and use it as a stepping stone to solve the real {problem} in the future."
    agent2.backstory = "well educated scientist with general good understanding of the topic. Known for his reliability and ability to simplify problems to their core. But not especially creative or an expert in the {problem} at hand."
    agent2.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is especially important for the model maker agent, because it needs to provide a detailed description of the simple model that can be quite long, and also include the solution which can also be quite long; without setting this, the agent might not be able to provide a complete description of the model and its solution, which would make it harder for the other agents to work with it and also limit the performance of the whole crew in solving the problem.

    task2 : Tasks = orchestration.createTask(name = "Simple Model Creation",
                                             description="Propose a simple model that is somewhat similar to the real {problem} but simpler to solve, based on the information provided by the information gatherer. The model should have already been solved in the literature, so the agent can find the solution and use it as a stepping stone to solve the real {problem} in the future.",
                                             agent=agent2,
                                             expected_output="A description of the simple model, that can be understood and worked with by other agents. The description should be mathematically precise and include the solution. It should be in a way, that another agent can create a simmulation based on the description.")


    agent3 : Agents = orchestration.createAgent(model="devstral-2-123b-instruct-2512", name = "simulator", role="simulate the simple model")
    agent3.goal = "simulate the simple model proposed by the model maker for the {problem}. The simulation should be as accurate as possible given the limitations of the model. But also efficient enough to run in a reasonable time frame. The results of the simulation should be analyzed and visualized to provide insights into the behavior of the model."
    agent3.backstory = "well trained in scienctific computing and simulations. Known for his reliable simulations and accurate coding. Likes to write pyhton code so others can easily understand and work with it."
    agent3.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the simulator agent, because it needs to provide a detailed simulation code that can be quite long, especially if the simple model is complex; without setting this, the agent might not be able to provide a complete simulation code, which would make it harder for the analyzer agent to work with it and also limit the performance of the whole crew in solving the problem.

    task3 : Tasks = orchestration.createTask(name = "Simulation of the simple model",
                                             description="Simulate the simple model proposed by the model maker for the {problem}. The simulation should be as accurate as possible given the limitations of the model. But also efficient enough to run in a reasonable time frame. The results of the simulation should be analyzed and visualized to provide insights into the behavior of the model.",
                                             agent=agent3,
                                             expected_output="Python code that simulates the simple model. The code should be well documented and include comments explaining the different steps. The results of the simulation should be visualized in a way that provides insights into the behavior of the model, e.g. through plots or animations.")
    

    agent4 : Agents = orchestration.createAgent(model="qwen3.5-397b-a17b", name = "summarizer & analyzer", role="analyze the results of the model maker and the simulation and summarizes it in a way a human researcher can understand")
    agent4.goal = "create a result that a human researcher can understand and work with, as well as reproduce."
    agent4.backstory = "a good analyzer and summarizer who can explain complex scientific results and ideas in a way that a more practically oriented scientist can understand and work with. Not an expert in the specific problem at hand, but good at understanding and summarizing scientific results in general."
    agent4.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the analyzer agent, because it needs to provide a detailed analysis and summary of the results that can be quite long, especially if the simple model and its simulation are complex; without setting this, the agent might not be able to provide a complete analysis and summary, which would make it harder for a human researcher to understand and work with the results, and also limit the performance of the whole crew in solving the problem.

    task4 : Tasks = orchestration.createTask(name = "Analysis and summarization of the results",
                                             description="Analyze the results of the model maker and the simulation and summarize it in a way   a human researcher can understand. The summary should include the insights gained from the model and the simulation, as well as any limitations or assumptions that were made. The summary should be concise but informative enough for a human researcher to understand and work with it.",
                                             agent=agent4,
                                             expected_output="A summary of the results of the model maker and the simulation for the {problem}, that a human researcher can understand and work with. The summary should include the insights gained from the model and the simulation, as well as any limitations or assumptions that were made. Summary should include the simualtion code and the result of it.")


    crew : Crews = orchestration.createCrew(verbose=True)
    result = orchestration.runCrew(problem="Why is the speed of light a constant in a vacuum?", 
                                   goal="provide a comprehensive answer to the question.", 
                                   data={})
    print(result.raw)