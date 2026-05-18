from datetime import datetime

from physicsmodellinghelperCustomSim.main import run
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
                'Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity) and display the relations.'
    }
    run(inputs = inputs, outputNr = 5, outputDir = "runOutputsCustomSim/")

if __name__ == "__main__":
    inputExplicitPlot()