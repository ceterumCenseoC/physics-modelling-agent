#here problems are specified in methods that return a dict

def blackHoleEffect() -> dict:
    concreteProblem = "How does the presence of a black hole affect the orbit of a nearby star?"
    concreteData = {}
    argumentsDict = {"problem" : concreteProblem, "goal" : "Solve the problem by creating a simple model, simulating it and analyzing the results. Provide a summary of the results that a human researcher can understand and work with.", "data" : concreteData}
    
    return argumentsDict

def edelsteinEffectNoSimulation() -> dict:
    topic = "Edelstein effect in Kramers-Weyl fermions"
    concreteProblem = "Calculate the Edelstein effect for a Kramers-Weyl fermion at the Gamma point of the Brillouin zone. Compute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field. Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity)"
    argumentsDict = {"topic" : topic, "problem" : concreteProblem, "simulation" : False}
    return argumentsDict

def edelsteinEffectWithSimulation() -> dict:
    topic = "Edelstein effect in Kramers-Weyl fermions"
    concreteProblem = "Calculate the Edelstein effect for a Kramers-Weyl fermion at the Gamma point of the Brillouin zone. Compute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field. Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity)"
    argumentsDict = {"topic" : topic, "problem" : concreteProblem, "simulation" : True}
    return argumentsDict
