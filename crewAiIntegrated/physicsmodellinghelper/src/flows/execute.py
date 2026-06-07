from datetime import datetime

from flows.main import run
def input12():
    inputs = {
        'topic': 'Edelstein-Effect',
        'current_time': str(datetime.now()),
        'aim': 'Calculate the Edelstein effect for a Rashba fermion (at the Gamma point of the Brillouin zone).' #THIS IS THE CURRENT AIM FOR GETTING A FIRST MODEL
                'Compute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field. '
                'Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity) and display the relations'
    }
    run(inputs = inputs, outputNr = 12, outputDir = "runOutputs/")

def inputExplicitPlot():
    inputs = {
        'topic': 'Edelstein-Effect',
        'current_time': str(datetime.now()),
        'aim': 'Calculate the Edelstein effect for a Rashba fermion (at the Gamma point of the Brillouin zone). ' #THIS IS THE CURRENT AIM FOR GETTING A FIRST MODEL
                'Compute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field. '
                'Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity) and make explicit graphics.'
    }
    run(inputs = inputs, outputNr = 6, outputDir = "runOutputsCustomSim/")

def runCrewModelling(topic : str, aim : str, ouputNr : int, outputDir : str, previous_output : dict):
    inputs = {
        'topic': topic,
        'aim': aim,
        'previous_output': previous_output
    }
    run(inputs = inputs, outputNr = ouputNr, outputDir = outputDir)

if __name__ == "__main__":
    inputMoreDeterministic()