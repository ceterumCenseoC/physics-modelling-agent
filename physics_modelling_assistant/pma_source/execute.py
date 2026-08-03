import json # use for converting raw output of the crew to a dictionary

from .sourceFinding.main import run_crew_paperFinder
from .modelling.main import run_crew_modelling

def listModels() -> list:
    '''
    This method can be used to list available models from the AI service.
    '''
    import os
    from dotenv import load_dotenv
    from pathlib import Path
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
    apiKey = os.getenv("API_KEY")

    import openai
    client = openai.OpenAI(
        api_key=apiKey,
        base_url="https://chat-ai.academiccloud.de/v1"
    )
    
    models = client.models.list().data
    modelList : list[str] = []
    for m in models:
        modelList.append(m.id)
    return modelList

class Physics_Modelling_Assistant(Model):
    def findPapers(self, topic : str, aim : str, outputDir : str, pdfSaveDir : str):
        inputs = {
            'topic': topic,
            'aim': aim
        }
        result = run_crew_paperFinder(inputs = inputs, outputDir = outputDir, pdfSaveDir = pdfSaveDir)
        return result

    def buildModel(self, topic : str, aim : str, outputDir : str, pdfSaveDir : str, previous_output : str):
        inputs = {
            'topic': topic,
            'aim': aim,
            'previous_output': previous_output
        }
        result = run_crew_modelling(inputs = inputs, outputDir = outputDir, pdfSaveDir = pdfSaveDir)
        return result

    def findAndBuild(self, topic : str, aim : str, outputDir : str, pdfSaveDir : str):
        inputs = {
            'topic': topic,
            'aim': aim
        }
        result = run_crew_paperFinder(inputs = inputs, outputDir = outputDir, pdfSaveDir = pdfSaveDir)
        inputs2 = {
            'topic': topic,
            'aim': aim,
            'previous_output': result.raw
        }
        outputDir = outputDir +  f"/version_1/"
        result2 = run_crew_modelling(inputs = inputs2, outputDir = outputDir, pdfSaveDir = pdfSaveDir)
        return result, result2

    def execute(self):
        """
        this method runs the acctual crew
        change
        """
        topic = 'Edelstein-Effect'
        aim = 'Calculate the Edelstein effect for a Rashba fermion (at the Gamma point of the Brillouin zone). ' \
            'Compute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field. '\
            'Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity, spin-orbit coupling strength) and make explicit graphics.'
        
        outputNr = 1 # CHANGE THIS NUMBER WHEN YOU START A NEW RUN WITH NEW PAPER SEARCH

        outputDir = f"./partialExecutionOutputs/runNr_{outputNr}/"
        pdfSaveDir = f"./partialExecutionOutputs/runNr_{outputNr}/pdfs"

        resultPapers = findPapers(topic = topic, aim = aim, outputDir = outputDir, pdfSaveDir = pdfSaveDir)
        with open(f"{outputDir}/result_papers.txt", "w") as f:
            f.write(resultPapers.raw)
        previous_output = resultPapers.raw
        previous_output = None
        
        versionNr = 9 # CHANGE THIS NUMBER WHEN YOU WANT TO KEEP THE PDF'S AND CHANGE THE MODELLING CREW
        buildModel(topic = topic, aim = aim, outputDir = outputDir + f"/version_{versionNr}/", pdfSaveDir = pdfSaveDir, previous_output = previous_output)
        """
        versionNr += 1
        buildModel(topic = topic, aim = aim, outputDir = outputDir + f"/version_{versionNr}/", pdfSaveDir = pdfSaveDir, previous_output = previous_output)
        versionNr += 2
        buildModel(topic = topic, aim = aim, outputDir = outputDir + f"/version_{versionNr}/", pdfSaveDir = pdfSaveDir, previous_output = previous_output)
        """

    def convertToDict(self, inStr : str) -> dict:
        """
        this method converts the output of the crew to a dictionary
        """
        return json.loads(inStr)    

    def executeInterface(self, topic : str, aim : str, outputDir : str, pdfSaveDir : str, versionNr : int) -> str:
        """
        this method allows for another programm to access and run the crew. Necessary for evaluation
        """
        resultPapers = findPapers(topic = topic, aim = aim, outputDir = outputDir, pdfSaveDir = pdfSaveDir)
        """ with open(f"{outputDir}/result_papers.txt", "w") as f:
            f.write(resultPapers.raw)
        """
        """ if previous_output is None:
            previous_output = resultPapers.raw"""
        previous_output = None
        
        resultModel = self.buildModel(topic = topic, aim = aim, outputDir = outputDir + f"/version_{versionNr}/", pdfSaveDir = pdfSaveDir, previous_output = previous_output)
        return resultModel.raw # only a string 

########################################################
# FOR CRITPT EVALUATION
########################################################
from inspect_ai.model import ModelAPI, ModelOutput, ChatMessage, ToolInfo, ToolChoice, GenerateConfig

class CritPtExposeAPI(ModelAPI):
    __registry_name__ = "pma"  # This is the name that will be used to register the model in the registry   
    def __init__(self, model_name: str, **model_args):
        super().__init__(model_name, **model_args)
        self.agent = Physics_Modelling_Assistant(**model_args)

    async def generate(self, input, tools=None, tool_choice = None, config=None, cache=None) -> ModelOutput:
        # latest user message
        user_input = input[-1].content

        # run your agent pipeline
        output = await self.agent.executeInterface(topic="", aim=user_input, outputDir="./critPt/eval/", pdfSaveDir="./critPt/eval/pdfs", versionNr=1)

        # return Inspect-compatible output
        # investigate how this object really works
        return ModelOutput(choices=[ToolChoice(message=ChatMessage(role="assistant", content=output))])
        return {
            "role": "assistant",
            "content": output
        }

if __name__ == "__main__":
    print("Available models: ", listModels())
    pma = Physics_Modelling_Assistant()
    pma.execute()
    #inStr = '{\n"choices": [\n {\n "message": {\n "content": "50.7 atm"\n }\n }\n ]\n }\n'
    #convertToDict(inStr)