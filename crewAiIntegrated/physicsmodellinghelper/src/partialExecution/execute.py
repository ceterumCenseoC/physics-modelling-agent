from partialExecution.sourceFinding.main import run_crew_paperFinder
from partialExecution.modelling.main import run_crew_modelling

def findPapers(topic : str, aim : str, outputDir : str, pdfSaveDir : str):
    inputs = {
        'topic': topic,
        'aim': aim
    }
    result = run_crew_paperFinder(inputs = inputs, outputDir = outputDir, pdfSaveDir = pdfSaveDir)
    return result

def buildModel(topic : str, aim : str, outputDir : str, pdfSaveDir : str, previous_output : str):
    inputs = {
        'topic': topic,
        'aim': aim,
        'previous_output': previous_output
    }
    result = run_crew_modelling(inputs = inputs, outputDir = outputDir, pdfSaveDir = pdfSaveDir)
    return result

def findAndBuild(topic : str, aim : str, outputDir : str, pdfSaveDir : str):
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

def execute():
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

    """ resultPapers = findPapers(topic = topic, aim = aim, outputDir = outputDir, pdfSaveDir = pdfSaveDir)
    with open(f"{outputDir}/result_papers.txt", "w") as f:
          f.write(resultPapers.raw)
    previous_output = resultPapers.raw """
    previous_output = None
    
    versionNr = 9 # CHANGE THIS NUMBER WHEN YOU WANT TO KEEP THE PDF'S AND CHANGE THE MODELLING CREW
    buildModel(topic = topic, aim = aim, outputDir = outputDir + f"/version_{versionNr}/", pdfSaveDir = pdfSaveDir, previous_output = previous_output)
    """
    versionNr += 1
    buildModel(topic = topic, aim = aim, outputDir = outputDir + f"/version_{versionNr}/", pdfSaveDir = pdfSaveDir, previous_output = previous_output)
    versionNr += 2
    buildModel(topic = topic, aim = aim, outputDir = outputDir + f"/version_{versionNr}/", pdfSaveDir = pdfSaveDir, previous_output = previous_output)
    """

if __name__ == "__main__":
    execute()