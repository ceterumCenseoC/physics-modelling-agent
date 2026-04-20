#here problems are specified in methods that return a dict

def blackHoleEffect() -> dict:
    concreteProblem = "How does the presence of a black hole affect the orbit of a nearby star?"
    goal = "Solve the problem by creating a simple model, simulating it and analyzing the results. Provide a summary of the results that a human researcher can understand and work with."
    concreteData = {}
    argumentsDict = {"problem" : concreteProblem, "goal" : goal, "data" : concreteData, "simulation" : "False"}
    
    return argumentsDict

def edelsteinEffectNoSimulation() -> dict:
    topic = "Edelstein effect in Kramers-Weyl fermions"
    concreteProblem = "Calculate the Edelstein effect for a Kramers-Weyl fermion at the Gamma point of the Brillouin zone. Compute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field. Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity)"
    argumentsDict = {"topic" : topic, "problem" : concreteProblem + "WITHOUT SIMULATION"}

    return argumentsDict

def edelsteinEffectWithSimulation() -> dict:
    topic = "Edelstein effect in Kramers-Weyl fermions"
    concreteProblem = "Calculate the Edelstein effect for a Kramers-Weyl fermion at the Gamma point of the Brillouin zone. Compute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field. Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity)"
    argumentsDict = {"topic" : topic, "problem" : concreteProblem + "WITH SIMULATION"}
    return argumentsDict

def edelsteinEffectResourceGathering() -> dict:
    topic = "Edelstein effect in Kramers-Weyl fermions"
    concreteProblem = "Gather sources abut how to calculate the Edelstein effect for a Kramers-Weyl fermion at the Gamma point of the Brillouin zone. The sources should include how to compute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field."
    argumentsDict = {"topic" : topic, "problem" : concreteProblem}
    return argumentsDict

def goldPrice() -> dict:
    topic = "gold price"
    concreteProblem = "What is the current gold price? From which date is this the gold price?"
    argumentsDict = {"topic" : topic, "problem" : concreteProblem, "website" : "https://goldprice.org/"}
    return argumentsDict

def date() -> dict:
    concreteProblem = "What is the current date?"
    argumentsDict = {"problem" : concreteProblem}
    return argumentsDict

def toolCheck() -> dict:
    concreteProblem = "Last 400 chars: of https://www.berkshirehathaway.com/"
    argumentsDict = {"problem" : concreteProblem}
    return argumentsDict