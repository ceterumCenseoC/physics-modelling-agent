def listModels() -> None:
    from src.wrappersCrewAi.aiAccess.openAiClient import OpenAiClient
    saia = OpenAiClient()
    print(saia.listModels()) # prints the list of available models from the AI service

def crew1BlackHole() -> None:
    import problems.problemExamples as problemExamples
    import preparedCrews.simpleCrews as simpleCrews

    result = simpleCrews.crew1Execute(problemExamples.blackHoleEffect())
    print (result)

def crew2EdelsteinEffectNoSimulation() -> None:
    import problems.problemExamples as problemExamples
    import preparedCrews.simpleCrews as simpleCrews

    result = simpleCrews.crew2Execute(problemExamples.edelsteinEffectNoSimulation())
    print (result)

def crew3EdelsteinEffectWithSimulation() -> None:
    import problems.problemExamples as problemExamples
    import preparedCrews.simpleCrews as simpleCrews

    result = simpleCrews.crew2Execute(problemExamples.edelsteinEffectWithSimulation())
    print (result)


if __name__ == "__main__":
    #listModels()
    #crew1BlackHole()
    crew2EdelsteinEffectNoSimulation()
    #crew3EdelsteinEffectWithSimulation()