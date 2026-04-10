def listModels() -> None:
    from src.wrappersCrewAi.aiAccess.openAiClient import OpenAiClient
    saia = OpenAiClient()
    print(saia.listModels()) # prints the list of available models from the AI service

def crew1BlackHole() -> None:
    import problems.problemExample1 as problemExample1
    import preparedCrews.simpleCrew1 as simpleCrew1

    result = simpleCrew1.crew1Execute(problemExample1.blackHoleEffect())
    print (result)


if __name__ == "__main__":
    listModels()
    crew1BlackHole()