from datetime import datetime

from physicsModellingWithSummary.main import run
if __name__ == "__main__":
    inputs = {
        'topic': 'Edelstein-Effect',
        'current_time': str(datetime.now()),
        'aim': 'Calculate the Edelstein effect for a Rashba fermion (at the Gamma point of the Brillouin zone).' #THIS IS THE CURRENT AIM FOR GETTING A FIRST MODEL
                'Compute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field. '
                'Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity)'
    }
    run(inputs = inputs, outputNr = 1, outputDir = "critPt/")