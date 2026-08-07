import json # use for converting raw output of the crew to a dictionary
from datetime import datetime
import os # to track how long execution takes

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

class Physics_Modelling_Assistant:
    def findPapers(self, aim : str, outputDir : str, pdfSaveDir : str, temperature: float, top_p: float, max_tokens: int, max_iter: int, reasoning: bool, max_reasoning_attempts: int):
        inputs = { # this style allows to pass future key-value parirs like previous_output or othe additional information
            'aim': aim
        }
        result = run_crew_paperFinder(inputs = inputs, outputDir = outputDir, pdfSaveDir = pdfSaveDir, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = reasoning, max_reasoning_attempts = max_reasoning_attempts)
        return result

    def buildModel(self, aim : str, outputDir : str, pdfSaveDir : str, previous_output : str, temperature: float, top_p: float, max_tokens: int, max_iter: int, reasoning : bool, max_reasoning_attempts: int):
        inputs = { # this style allows to pass future key-value parirs like previous_output or othe additional information
            'aim': aim,
            'previous_output': previous_output
        }
        result = run_crew_modelling(inputs = inputs, outputDir = outputDir, pdfSaveDir = pdfSaveDir, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = reasoning, max_reasoning_attempts = max_reasoning_attempts)
        return result

    def findAndBuild(self, aim : str, outputDir : str, pdfSaveDir : str, temperature: float, top_p: float, max_tokens: int, max_iter: int, reasoning: bool, max_reasoning_attempts: int):
        inputs = { # this style allows to pass future key-value parirs like previous_output or othe additional information
            'aim': aim
        }
        result = run_crew_paperFinder(inputs = inputs, outputDir = outputDir, pdfSaveDir = pdfSaveDir, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = False, max_reasoning_attempts = 1)
        inputs2 = { # this style allows to pass future key-value parirs like previous_output or othe additional information
            'aim': aim,
            'previous_output': result.raw
        }
        outputDir = outputDir +  f"/version_1/"
        result2 = run_crew_modelling(inputs = inputs2, outputDir = outputDir, pdfSaveDir = pdfSaveDir, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = reasoning, max_reasoning_attempts = max_reasoning_attempts)
        return result, result2

    def execute(self):
        """
        this method runs the acctual crew
        change
        """
        aim = 'Calculate the Edelstein effect for a Rashba fermion (at the Gamma point of the Brillouin zone). ' \
            'Compute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field. '\
            'Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity, spin-orbit coupling strength) and make explicit graphics.'
        
        outputNr = 1 # CHANGE THIS NUMBER WHEN YOU START A NEW RUN WITH NEW PAPER SEARCH
        versionNr = 1 # CHANGE THIS NUMBER WHEN YOU WANT TO KEEP THE PDF'S AND CHANGE THE MODELLING CREW
        outputDir = f"./pmaOUT/runNr_{outputNr}/"+ f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}/"
        pdfSaveDir = f"./pmaOUT/runNr_{outputNr}/pdfs" + f"_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

        temperature = 0.95
        top_p = 0.8
        max_tokens = 50_000
        max_iter = 3
        reasoning = True #reasoning false for source finding, true for modelling
        max_reasoning_attempts = 3

        startTime = datetime.now()
        with open(f"time.txt", "a") as f:
            f.write(f"Run Number {outputNr}, Start time: {startTime}\n")
        resultPapers = self.findPapers(aim = aim, outputDir = outputDir, pdfSaveDir = pdfSaveDir, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = False, max_reasoning_attempts = 1)
        """ with open(f"{outputDir}/result_papers.txt", "w") as f:
            f.write(resultPapers.raw)
        previous_output = resultPapers.raw """
        previous_output = None

        resultModel = self.buildModel(aim = aim, outputDir = outputDir + f"/version_{versionNr}/", pdfSaveDir = pdfSaveDir, previous_output = previous_output, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = reasoning, max_reasoning_attempts = max_reasoning_attempts)
        finalTime = datetime.now()
        with open(f"time.txt", "a") as f:
            f.write(f"Run Number {outputNr}, Final time: {finalTime}\n")
        with open(f"executionDuration.txt", "a") as f:
            f.write(f"Execution took {finalTime - startTime} time.\n")
        print(f"Execution took {finalTime - startTime} time.")
        print(type(resultModel))
        print(resultModel.raw) # only a string
        import requests
        requests.post(os.getenv("DISCORD_WEBHOOK_URL"), json={"content": "Your Python script has finished!"})

    def convertToDict(self, inStr : str) -> dict:
        """
        this method converts the output of the crew to a dictionary
        """
        return json.loads(inStr)    

    def executeInterface(self, id : str, aim : str, outputDir : str, pdfSaveDir : str, versionNr : int, temperature: float, top_p: float, max_tokens: int, max_iter: int, reasoning: bool, max_reasoning_attempts: int) -> str:
        """
        this method allows for another programm to access and run the crew. Necessary for evaluation
        """
        ####TEST
        import logging, traceback, inspect, sys

        logger = logging.getLogger("llm-debug")
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(handler)
        ####TEST
        formatted = id

        outputDir = outputDir + f"{formatted}/"
        pdfSaveDir = pdfSaveDir + f"_{formatted}"
        print("Finding papers")
        # paper finder uses no reasoning, because it is not necessary to reason about the papers, but only to find them

        try:
            resultPapers = self.findPapers(aim = aim, outputDir = outputDir, pdfSaveDir = pdfSaveDir, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = 1, reasoning = False, max_reasoning_attempts = 1)
            """ with open(f"{outputDir}/result_papers.txt", "w") as f:
                f.write(resultPapers.raw)
            """
            """ if previous_output is None:
                previous_output = resultPapers.raw"""
            previous_output = None
            print("Building model")
            resultModel = self.buildModel(aim = aim, outputDir = outputDir, pdfSaveDir = pdfSaveDir, previous_output = previous_output, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = reasoning, max_reasoning_attempts = max_reasoning_attempts)
            print(resultModel.raw) # only a string
            return resultModel.raw # only a string 

        except Exception as e:
            logger.error("Exception repr: %r", e)
            logger.error("Exception type: %s", type(e))
            logger.error("Exception module: %s", getattr(type(e), '__module__', None))
            logger.error("Traceback:\n%s", traceback.format_exc())
            print("TRY STH NEW")
            try:
                logger.error("Exception class source: %s", inspect.getsourcefile(type(e)))
            except Exception:
                logger.error("Could not determine source file for exception class")
            raise

    def executeInterfaceShortcut(self, id : str, aim : str, outputDir : str, pdfSaveDir : str, versionNr : int, temperature: float, top_p: float, max_tokens: int, max_iter: int, reasoning: bool, max_reasoning_attempts: int) -> str:
        """
        this method allows for another programm to access and run the crew. Necessary for evaluation
        """
        outputDir = outputDir + f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}/"
        pdfSaveDir = pdfSaveDir + f"_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
        # paper finder uses no reasoning, because it is not necessary to reason about the papers, but only to find them
        """ resultPapers = self.findPapers(aim = aim, outputDir = outputDir, pdfSaveDir = pdfSaveDir, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = False, max_reasoning_attempts = 1)
        previous_output = None
        print("Building model")
        resultModel = self.buildModel(aim = aim, outputDir = outputDir, pdfSaveDir = pdfSaveDir, previous_output = previous_output, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = reasoning, max_reasoning_attempts = max_reasoning_attempts)
        """
        return aim + " (shortcut) Result" # only a string 

########################################################
# FOR CRITPT EVALUATION
########################################################

if __name__ == "__main__":
    print("Available models: ", listModels())
    pma = Physics_Modelling_Assistant()
    pma.execute()
    #inStr = '{\n"choices": [\n {\n "message": {\n "content": "50.7 atm"\n }\n }\n ]\n }\n'
    #convertToDict(inStr)