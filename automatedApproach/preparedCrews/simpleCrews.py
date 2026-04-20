#pre prepared crew that can be called on a task passing a dict to it

from src.crewOrchestration import CrewOrchestration
from src.wrappersCrewAi.agents import Agents
from src.wrappersCrewAi.tasks import Tasks
from src.wrappersCrewAi.crews import Crews

#this is a crew setup finding sources, creating a simple model, simulating and then analyzing the result

""" models:
for information gateher: qwen3.5-122b-a10b
for physics & logic: deepseek-r1-distill-llama-70b
for coding: devstral-2-123b-instruct-2512
for general puprose: qwen3.5-397b-a17b """

def crew1Execute(argumentsDict : dict) -> str:
    # argumentsDict specifies the concrete problem/goal/... the crew is running on
    #returns the entire crews result as a string

    orchestration = CrewOrchestration()

    #INFORMATION GATHERER AGENT
    agent1 : Agents = orchestration.createAgent(model="qwen3.5-122b-a10b", name = "information gatherer", role="gather information about the {problem}")
    agent1.goal = "find 2-5 relevant pieces of information about the {problem} that will help solving it. Preferably scientific papers or books"
    agent1.backstory = "well educated scientist knowing the common approaches to most physics problems, but not an expert in the specific {problem} at hand. Does the groundwork so other agents can shine."
    agent1.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the information gatherer agent, because it needs to provide a detailed description of the relevant information that can be quite long, especially if the problem is complex; without setting this, the agent might not be able to provide a complete description of the relevant information, which would make it harder for the other agents to work with it and also limit the performance of the whole crew in solving the problem.

    task1 : Tasks = orchestration.createTask(name = "Information Gathering", 
                                             description="Find information about the scientific {problem} at hand. Filter for relevance and quality.", agent=agent1, 
                                             expected_output="A description of the relevant approaches (and information) to the {problem}, preferably with links to scientific papers or books. The description should be concise but informative enough for other agents to work with it.")
    
    #SIMPL MODEL MAKER AGENT
    agent2 : Agents = orchestration.createAgent(model="deepseek-r1-distill-llama-70b", name = "simple model maker", role="make simple model for the {problem}")
    agent2.goal = "propose a simple model that is somewhat similar to the real {problem} but simpler to solve, based on the information provided by the information gatherer. The model should have already been solved in the literature, so the agent can find the solution and use it as a stepping stone to solve the real {problem} in the future."
    agent2.backstory = "well educated scientist with general good understanding of the topic. Known for his reliability and ability to simplify problems to their core. But not especially creative or an expert in the {problem} at hand."
    agent2.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is especially important for the model maker agent, because it needs to provide a detailed description of the simple model that can be quite long, and also include the solution which can also be quite long; without setting this, the agent might not be able to provide a complete description of the model and its solution, which would make it harder for the other agents to work with it and also limit the performance of the whole crew in solving the problem.

    task2 : Tasks = orchestration.createTask(name = "Simple Model Creation",
                                             description="Propose a simple model that is somewhat similar to the real {problem} but simpler to solve, based on the information provided by the information gatherer. The model should have already been solved in the literature, so the agent can find the solution and use it as a stepping stone to solve the real {problem} in the future.",
                                             agent=agent2,
                                             expected_output="A description of the simple model, that can be understood and worked with by other agents. The description should be mathematically precise and include the solution. It should be in a way, that another agent can create a simmulation based on the description.")

    #PYTHON SIMULATION AGENT
    agent3 : Agents = orchestration.createAgent(model="devstral-2-123b-instruct-2512", name = "simulator", role="simulate the simple model")
    agent3.goal = "simulate the simple model proposed by the model maker for the {problem}. The simulation should be as accurate as possible given the limitations of the model. But also efficient enough to run in a reasonable time frame. The results of the simulation should be analyzed and visualized to provide insights into the behavior of the model."
    agent3.backstory = "well trained in scienctific computing and simulations. Known for his reliable simulations and accurate coding. Likes to write pyhton code so others can easily understand and work with it."
    agent3.max_tokens = 131072 - 7000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the simulator agent, because it needs to provide a detailed simulation code that can be quite long, especially if the simple model is complex; without setting this, the agent might not be able to provide a complete simulation code, which would make it harder for the analyzer agent to work with it and also limit the performance of the whole crew in solving the problem.

    task3 : Tasks = orchestration.createTask(name = "Simulation of the simple model",
                                             description="Simulate the simple model proposed by the model maker for the {problem}. The simulation should be as accurate as possible given the limitations of the model. But also efficient enough to run in a reasonable time frame. The results of the simulation should be analyzed and visualized to provide insights into the behavior of the model.",
                                             agent=agent3,
                                             expected_output="Python code that simulates the simple model. The code should be well documented and include comments explaining the different steps. The results of the simulation should be visualized in a way that provides insights into the behavior of the model, e.g. through plots or animations.")
    
    #ANALYZER AGENT
    agent4 : Agents = orchestration.createAgent(model="qwen3.5-397b-a17b", name = "summarizer & analyzer", role="analyze the results of the model maker and the simulation and summarizes it in a way a human researcher can understand")
    agent4.goal = "create a result that a human researcher can understand and work with, as well as reproduce."
    agent4.backstory = "a good analyzer and summarizer who can explain complex scientific results and ideas in a way that a more practically oriented scientist can understand and work with. Not an expert in the specific problem at hand, but good at understanding and summarizing scientific results in general."
    agent4.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the analyzer agent, because it needs to provide a detailed analysis and summary of the results that can be quite long, especially if the simple model and its simulation are complex; without setting this, the agent might not be able to provide a complete analysis and summary, which would make it harder for a human researcher to understand and work with the results, and also limit the performance of the whole crew in solving the problem.

    task4 : Tasks = orchestration.createTask(name = "Analysis and summarization of the results",
                                             description="Analyze the results of the model maker and the simulation and summarize it in a way   a human researcher can understand. The summary should include the insights gained from the model and the simulation, as well as any limitations or assumptions that were made. The summary should be concise but informative enough for a human researcher to understand and work with it.",
                                             agent=agent4,
                                             expected_output="A summary of the results of the model maker and the simulation for the {problem}, that a human researcher can understand and work with. The summary should include the insights gained from the model and the simulation, as well as any limitations or assumptions that were made. Summary should include the simualtion code and the result of it.")

    crew : Crews = orchestration.createCrew(verbose=True)

    result = orchestration.runCrew(argumentsDict) # put the argumentsDict here to make sure the crew has access to the problem, goal, ...

    return(result.raw)

def crew2Execute(argumentsDict : dict) -> str:
    #this is a different crew with edited texts for better syntax; optimised for edelstein-Effect
    
    orchestration = CrewOrchestration()

    #iINFORMATION GATHERER AGENT
    infoGatherer1 : Agents = orchestration.createAgent(model="qwen3.5-122b-a10b", name = "information gather", role="information gatherer for: {problem}")
    infoGatherer1.goal = "find relevant information for the following problem: {problem}. The retrieved information should allow for following agents to modell the problem. Find 2-5 scientific papers or books."
    infoGatherer1.backstory = "well educated scientist having good knowledge with the {topic}, but not an expert in the specific {problem} at hand. Does the groundwork so other agents can shine. Likes to use arxiv."
    #infoGatherer1.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the information gatherer agent, because it needs to provide a detailed description of the relevant information that can be quite long, especially if the problem is complex; without setting this, the agent might not be able to provide a complete description of the relevant information, which would make it harder for the other agents to work with it and also limit the performance of the whole crew in solving the problem.

    infoGathering1 : Tasks = orchestration.createTask(name = "Information Gathering", 
                                             description="Find information about the scientific {problem} at hand. Filter for relevance and quality.", agent=infoGatherer1, 
                                             expected_output="A description of the relevant approaches (and information) to the {problem}, preferably with the URL to scientific papers or books. The description should be concise but informative enough for other agents to work with it.")
    

    #SIMPL MODEL MAKER AGENT
    simpleModeler1 : Agents = orchestration.createAgent(model="deepseek-r1-distill-llama-70b", name = "simple model maker 1", role="make simple model for the problem: {problem}")
    simpleModeler1.goal = "create a simpler model for the following problem: {problem}. The model should be simpler to solve than the real problem and should also reproduce known results from the literature. The model should be based on the information provided by the information gatherer."
    simpleModeler1.backstory = "scientist with a good understanding of the {topic}. Is excellent in creating reliable and simple models from given information. Is not creative."
    #simpleModeller1.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is especially important for the model maker agent, because it needs to provide a detailed description of the simple model that can be quite long, and also include the solution which can also be quite long; without setting this, the agent might not be able to provide a complete description of the model and its solution, which would make it harder for the other agents to work with it and also limit the performance of the whole crew in solving the problem.

    simpleModeling1 : Tasks = orchestration.createTask(name = "Simple Model Creation",
                                             description="Propose a simple model that is somewhat similar to the actual problem: {problem}. The model should be simpler to solve and have an exisiting soulution in the literature. The model should be based on the information provided by the information gatherer to ensure its relevance.", agent=simpleModeler1,
                                             expected_output="The simple model with a textual description as well as a mathematical formulation. The output should include the solution of the simple model and allow later agents to create a simulation and also generalisation the the real problem: {problem}.")

    #todo: add a second model maker agent that creates a different simple model

    #NUMERICAL IMPLEMENTOR AGENT
    numericalImplementor1 : Agents = orchestration.createAgent(model="deepseek-r1-distill-llama-70b", name = "numerical implementor 1", role="make a numerical implementation of the simple model from simple model maker 1")
    numericalImplementor1.goal = "Create a numerical implementation which is only derived from the simple model 1. It should be precise and well-documented to allow others to understand the implementation and check it against results from the literature."
    numericalImplementor1.backstory = "scientist with a very good understanding of numerical methods and scientific computing. Very good at creating precise models with a consistent logic. Sticks to the provided information and will ask for clarification it needed."
    #numericalImplementor1.max_tokens = 131072 - 7000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the simulator agent, because it needs to provide a detailed simulation code that can be quite long, especially if the simple model is complex; without setting this, the agent might not be able to provide a complete simulation code, which would make it harder for the analyzer agent to work with it and also limit the performance of the whole crew in solving the problem.

    implementNumerically1 : Tasks = orchestration.createTask(name = "numerical implementation of the simple model 1",
                                             description="Implement the simple model proposed by the model maker 1 for the problem: {problem}. The implementation should be as accurate as possible given the limitations of the model.", agent = numericalImplementor1,
                                             expected_output="A mathematical formulation of the numerical implementation of the simple model 1. With explainations of the different steps and decisions made during the implementation. For formula output, use LaTeX format to ensure clarity and precision.")
    
    #todo: add a second numerical implementor agent that creates a different numerical implementation of the simple model 1, or an implementation of the second simple model if there is a second model maker agent

    #MODEL CHECKER AGENT
    modelChecker1 : Agents = orchestration.createAgent(model="deepseek-r1-distill-llama-70b", name = "validator 1", role="analyze the results of model maker 1 and the numerical implementor 1")
    modelChecker1.goal = "Check the results of the model maker 1 and the numerical implementor 1 for accuracy and consistency. Look out for any mistakes or inconsistencies. Compare the results of the simple model with known results from the literature. Use the literature provided by information gatherer 1."
    modelChecker1.backstory = "scientist with a very sharp logic. Is well educated with the {topic}. Is able to compare the logic and sense of physical approaches and results, not just the word similarity"
    #modelChecker1.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the analyzer agent, because it needs to provide a detailed analysis and summary of the results that can be quite long, especially if the simple model and its simulation are complex; without setting this, the agent might not be able to provide a complete analysis and summary, which would make it harder for a human researcher to understand and work with the results, and also limit the performance of the whole crew in solving the problem.

    checkModel1 : Tasks = orchestration.createTask(name = "check simple model 1 and its numerical implementation",
                                             description="Analyze the results of the model maker 1 and numerical implementor 1 for accuracy and consistency. Look out for any mistakes or inconsistencies. Compare the results of the simple model with known results from the literature. Use the literature provided by information gatherer 1.",
                                             agent=modelChecker1,
                                             expected_output="An analysis of the results of the model maker 1 and numerical implementor 1. Mentioning of relevant mistakes or inconsistencies. Comparison with literature results. Suggestion on how to improve the model and its implementatiion.")

    #todo: DECIDE IF AN AGENT SHOULD DECIDE FOR A RERUN WITH IMPROVED CREW AND SPECIFICATION


    #SIMULATION AGENT
    simulation1 : Agents = orchestration.createAgent(model="qwen3.5-397b-a17b", name = "simulation 1", role="create and run simulations of the simple model and it's numerical implementation as well as the literature")
    simulation1.goal = "create a simulation of the simple model and its numerical implementation as well as the literature. The simulation should be accurate but also efficient. The code should be tested and working." 
    simulation1.backstory = "a skilled simulation specialist with a strong background in computational physics. Has experience with various simulation tools and techniques. Known for is reliability and quality of code."

    simulate1 : Tasks = orchestration.createTask(name = "simulation of the simple model and its numerical implementation",
                                             description="Create a simulation of the simple model and its numerical implementation as well as the literature. The simulation should be accurate but also efficient. The code should be tested and working.", agent=simulation1,
                                             expected_output="ONLY OUTPUT when simulation is requested. Python code that just needs to be copy pasted and run to get the simulaition results.")


    #REPORTER AGENT
    reporter1 : Agents = orchestration.createAgent(model="qwen3.5-397b-a17b", name = "reporter 1", role="reports results of the crew in a way a human researcher can understand and work with")
    reporter1.goal = "create a report that a human researcher can understand and work with. The report should include the relevant steps for reproducing the results, the evaluation on how well the simple model and its numerical implementation perform and the insights gained from the results."
    reporter1.backstory = "a good reporter who can explain complex scientific results and ideas in a way that a more practically oriented scientist can understand and work with. Not an expert in the specific problem: {problem}, but has good understanding for summarization and explanation."
    

    createReport1 : Tasks = orchestration.createTask(name = "create report of the results",
                                             description="Create a report that a human researcher can understand and work with. The report should include the relevant steps for reproducing the results, the evaluation on how well the simple model and its numerical implementation perform and the insights gained from the results.", agent=reporter1,
                                             expected_output="A report of the results that a human researcher can understand and work with. The report should include the relevant steps for reproducing the results, the evaluation on how well the simple model and its numerical implementation perform and the insights gained from the results. If formulas are included, use LaTeX format to ensure clarity and precision.")  

    crew : Crews = orchestration.createCrew(verbose=True)
    result = orchestration.runCrew(argumentsDict) # put the argumentsDict here to make sure the crew has access to the problem, goal, ...
    return(result.raw)


def crew3Execute(argumentsDict : dict) -> str:
    #this is a different crew with edited texts for better syntax; optimised for edelstein-Effect
    
    orchestration = CrewOrchestration()

    #iINFORMATION GATHERER AGENT
    infoGatherer1 : Agents = orchestration.createAgent(model="qwen3.5-122b-a10b", name = "information gather", role="information gatherer for: {problem}")
    infoGatherer1.goal = "find relevant information for the following problem: {problem}. The retrieved information should allow for following agents to modell the problem. Find 2-5 scientific papers or books."
    infoGatherer1.backstory = "well educated scientist having good knowledge with the {topic}, but not an expert in the specific {problem} at hand. Does the groundwork so other agents can shine. Likes to use arxiv."
    #infoGatherer1.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the information gatherer agent, because it needs to provide a detailed description of the relevant information that can be quite long, especially if the problem is complex; without setting this, the agent might not be able to provide a complete description of the relevant information, which would make it harder for the other agents to work with it and also limit the performance of the whole crew in solving the problem.

    infoGathering1 : Tasks = orchestration.createTask(name = "Information Gathering", 
                                             description="Find information about the scientific {problem} at hand. Filter for relevance and quality.", agent=infoGatherer1, 
                                             expected_output="A description of the relevant approaches (and information) to the {problem}, preferably with links to scientific papers or books. The description should be concise but informative enough for other agents to work with it.")
    

    #SIMPL MODEL MAKER AGENT
    simpleModeler1 : Agents = orchestration.createAgent(model="deepseek-r1-distill-llama-70b", name = "simple model maker 1", role="make simple model for the problem: {problem}")
    simpleModeler1.goal = "create a simpler model for the following problem: {problem}. The model should be simpler to solve than the real problem and should also reproduce known results from the literature. The model should be based on the information provided by the information gatherer."
    simpleModeler1.backstory = "scientist with a good understanding of the {topic}. Is excellent in creating reliable and simple models from given information. Is not creative."
    #simpleModeller1.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is especially important for the model maker agent, because it needs to provide a detailed description of the simple model that can be quite long, and also include the solution which can also be quite long; without setting this, the agent might not be able to provide a complete description of the model and its solution, which would make it harder for the other agents to work with it and also limit the performance of the whole crew in solving the problem.

    simpleModeling1 : Tasks = orchestration.createTask(name = "Simple Model Creation",
                                             description="Propose a simple model that is somewhat similar to the actual problem: {problem}. The model should be simpler to solve and have an exisiting soulution in the literature. The model should be based on the information provided by the information gatherer to ensure its relevance.", agent=simpleModeler1,
                                             expected_output="The simple model with a textual description as well as a mathematical formulation. The output should include the solution of the simple model and allow later agents to create a simulation and also generalisation the the real problem: {problem}.")

    #todo: add a second model maker agent that creates a different simple model

    #NUMERICAL IMPLEMENTOR AGENT
    numericalImplementor1 : Agents = orchestration.createAgent(model="deepseek-r1-distill-llama-70b", name = "numerical implementor 1", role="make a numerical implementation of the simple model from simple model maker 1")
    numericalImplementor1.goal = "Create a numerical implementation which is only derived from the simple model 1. It should be precise and well-documented to allow others to understand the implementation and check it against results from the literature."
    numericalImplementor1.backstory = "scientist with a very good understanding of numerical methods and scientific computing. Very good at creating precise models with a consistent logic. Sticks to the provided information and will ask for clarification it needed."
    #numericalImplementor1.max_tokens = 131072 - 7000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the simulator agent, because it needs to provide a detailed simulation code that can be quite long, especially if the simple model is complex; without setting this, the agent might not be able to provide a complete simulation code, which would make it harder for the analyzer agent to work with it and also limit the performance of the whole crew in solving the problem.

    implementNumerically1 : Tasks = orchestration.createTask(name = "numerical implementation of the simple model 1",
                                             description="Implement the simple model proposed by the model maker 1 for the problem: {problem}. The implementation should be as accurate as possible given the limitations of the model.", agent = numericalImplementor1,
                                             expected_output="A mathematical formulation of the numerical implementation of the simple model 1. With explainations of the different steps and decisions made during the implementation. For formula output, use LaTeX format to ensure clarity and precision.")
    
    #todo: add a second numerical implementor agent that creates a different numerical implementation of the simple model 1, or an implementation of the second simple model if there is a second model maker agent

    #MODEL CHECKER AGENT
    modelChecker1 : Agents = orchestration.createAgent(model="deepseek-r1-distill-llama-70b", name = "validator 1", role="analyze the results of model maker 1 and the numerical implementor 1")
    modelChecker1.goal = "Check the results of the model maker 1 and the numerical implementor 1 for accuracy and consistency. Look out for any mistakes or inconsistencies. Compare the results of the simple model with known results from the literature. Use the literature provided by information gatherer 1."
    modelChecker1.backstory = "scientist with a very sharp logic. Is well educated with the {topic}. Is able to compare the logic and sense of physical approaches and results, not just the word similarity"
    #modelChecker1.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the analyzer agent, because it needs to provide a detailed analysis and summary of the results that can be quite long, especially if the simple model and its simulation are complex; without setting this, the agent might not be able to provide a complete analysis and summary, which would make it harder for a human researcher to understand and work with the results, and also limit the performance of the whole crew in solving the problem.

    checkModel1 : Tasks = orchestration.createTask(name = "check simple model 1 and its numerical implementation",
                                             description="Analyze the results of the model maker 1 and numerical implementor 1 for accuracy and consistency. Look out for any mistakes or inconsistencies. Compare the results of the simple model with known results from the literature. Use the literature provided by information gatherer 1.",
                                             agent=modelChecker1,
                                             expected_output="An analysis of the results of the model maker 1 and numerical implementor 1. Mentioning of relevant mistakes or inconsistencies. Comparison with literature results. Suggestion on how to improve the model and its implementatiion.")

    #todo: DECIDE IF AN AGENT SHOULD DECIDE FOR A RERUN WITH IMPROVED CREW AND SPECIFICATION


    #SIMULATION AGENT
    simulation1 : Agents = orchestration.createAgent(model="qwen3.5-397b-a17b", name = "simulation 1", role="create and run simulations of the simple model and it's numerical implementation as well as the literature")
    simulation1.goal = "create a simulation of the simple model and its numerical implementation as well as the literature. The simulation should be accurate but also efficient. The code should be tested and working." 
    simulation1.backstory = "a skilled simulation specialist with a strong background in computational physics. Has experience with various simulation tools and techniques. Known for is reliability and quality of code."

    simulate1 : Tasks = orchestration.createTask(name = "simulation of the simple model and its numerical implementation",
                                             description="Create a simulation of the simple model and its numerical implementation as well as the literature. The simulation should be accurate but also efficient. The code should be tested and working.", agent=simulation1,
                                             expected_output="ONLY OUTPUT when {simulation} == True. python code that just needs to be copy pasted and run to get the simulaition results.")


    #REPORTER AGENT
    reporter1 : Agents = orchestration.createAgent(model="qwen3.5-397b-a17b", name = "reporter 1", role="reports results of the crew in a way a human researcher can understand and work with")
    reporter1.goal = "create a report that a human researcher can understand and work with. The report should include the relevant steps for reproducing the results, the evaluation on how well the simple model and its numerical implementation perform and the insights gained from the results."
    reporter1.backstory = "a good reporter who can explain complex scientific results and ideas in a way that a more practically oriented scientist can understand and work with. Not an expert in the specific problem: {problem}, but has good understanding for summarization and explanation."
    

    createReport1 : Tasks = orchestration.createTask(name = "create report of the results",
                                             description="Create a report that a human researcher can understand and work with. The report should include the relevant steps for reproducing the results, the evaluation on how well the simple model and its numerical implementation perform and the insights gained from the results.", agent=reporter1,
                                             expected_output="A report of the results that a human researcher can understand and work with. The report should include the relevant steps for reproducing the results, the evaluation on how well the simple model and its numerical implementation perform and the insights gained from the results. If formulas are included, use LaTeX format to ensure clarity and precision.")  

    crew : Crews = orchestration.createCrew(verbose=True)
    result = orchestration.runCrew(argumentsDict) # put the argumentsDict here to make sure the crew has access to the problem, goal, ...
    return(result.raw)

def crew4Execute(argumentsDict : dict) -> str:
    #focuses on getting real sources and minimizing hallucinations; optimised for edelstein-Effect
    orchestration = CrewOrchestration()

    #iINFORMATION GATHERER AGENT
    infoGatherer1 : Agents = orchestration.createAgent(model="qwen3.5-122b-a10b", name = "source gather", role="find real scientific sources for: {problem}")
    infoGatherer1.goal = "gather 2 scientific sources for the following problem: {problem}. Provide the full title and author information. Show where the source was found."
    infoGatherer1.backstory = "Always checks that title and author information is consistent."
    #infoGatherer1.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the information gatherer agent, because it needs to provide a detailed description of the relevant information that can be quite long, especially if the problem is complex; without setting this, the agent might not be able to provide a complete description of the relevant information, which would make it harder for the other agents to work with it and also limit the performance of the whole crew in solving the problem.
    infoGatherer1.temperature = 0.0 # set temperature to 0 to minimize hallucinations

    infoGathering1 : Tasks = orchestration.createTask(name = "Source Gathering", 
                                             description="Gather 3 scientific sources for the problem: {problem}.", agent=infoGatherer1, 
                                             expected_output="A list of 3 relevant scientific sources with CORRECT author and title information.")
    
    crew : Crews = orchestration.createCrew(verbose=True)
    result = orchestration.runCrew(argumentsDict) # put the argumentsDict here to make sure the crew has access to the problem, goal, ...
    return(result.raw)

def crew5Execute(argumentsDict : dict) -> str:
    #check internet connection and access to real sources
    orchestration = CrewOrchestration()

    #iINFORMATION GATHERER AGENT
    infoGatherer1 : Agents = orchestration.createAgent(model="qwen3.5-122b-a10b", name = "stock market checker", role="checks stock prices")
    infoGatherer1.goal = "retrieve the current stock price for gold using this website: {website}."
    infoGatherer1.backstory = "Would tell if he cannot access the website or has no internet connection."
    #infoGatherer1.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the information gatherer agent, because it needs to provide a detailed description of the relevant information that can be quite long, especially if the problem is complex; without setting this, the agent might not be able to provide a complete description of the relevant information, which would make it harder for the other agents to work with it and also limit the performance of the whole crew in solving the problem.
    infoGatherer1.temperature = 0.0 # set temperature to 0 to minimize hallucinations

    infoGathering1 : Tasks = orchestration.createTask(name = "gold price checker", 
                                             description="check the gold price at {website}.", agent=infoGatherer1, 
                                             expected_output="the current gold price at the specified website.")
    
    crew : Crews = orchestration.createCrew(verbose=True)
    result = orchestration.runCrew(argumentsDict) # put the argumentsDict here to make sure the crew has access to the problem, goal, ...
    return(result.raw)

def crew6Execute(argumentsDict : dict) -> str:

    orchestration = CrewOrchestration()

    #iINFORMATION GATHERER AGENT
    infoGatherer1 : Agents = orchestration.createAgent(model="qwen3.5-122b-a10b", name = "current data checker", role="what is the current date")
    infoGatherer1.goal = "write the date and time (down to the hour) of Berlin)."
    infoGatherer1.backstory = "Would tell if he cannot access the website or has no internet connection."
    #infoGatherer1.max_tokens = 131072 - 3000 # set max response tokens to the maximum context length of the model minus some buffer for the input and the system prompt, to make sure the agent can use the full context length for the response if needed; this is important for the information gatherer agent, because it needs to provide a detailed description of the relevant information that can be quite long, especially if the problem is complex; without setting this, the agent might not be able to provide a complete description of the relevant information, which would make it harder for the other agents to work with it and also limit the performance of the whole crew in solving the problem.
    infoGatherer1.temperature = 0.0 # set temperature to 0 to minimize hallucinations

    infoGathering1 : Tasks = orchestration.createTask(name = "Date checker", 
                                             description="Solve the problem using your expertise.", agent=infoGatherer1, 
                                             expected_output="The current date and time in Berlin is DD.MM.YYYY, HH:MM.")
    
    crew : Crews = orchestration.createCrew(verbose=True)
    result = orchestration.runCrew(argumentsDict) # put the argumentsDict here to make sure the crew has access to the problem, goal, ...
    return(result.raw)

def crew7(argumentsDict : dict) -> str:
    #check if the crew can access the local file system
    orchestration = CrewOrchestration()

    #iINFORMATION GATHERER AGENT
    infoGatherer1 : Agents = orchestration.createAgent(model="qwen3.5-397b-a17b", name = "agent", role="do what the crew asks you to do")
    infoGatherer1.temperature = 0.0 # set temperature to 0 to minimize hallucinations

    infoGathering1 : Tasks = orchestration.createTask(name = "task", 
                                             description="works on: {problem}", agent=infoGatherer1, 
                                             expected_output="as specified in: {problem}.")
    
    crew : Crews = orchestration.createCrew(verbose=True)
    result = orchestration.runCrew(argumentsDict) # put the argumentsDict here to make sure the crew has access to the problem, goal, ...
    return(result.raw)
