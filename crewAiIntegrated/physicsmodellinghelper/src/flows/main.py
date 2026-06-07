#!/usr/bin/env python
import sys
import warnings

from flows.crew_paperFinder import PaperFinderCrew
from flows.crew_modelling import ModellerCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run_crew_paperFinder(inputs : dict, outputNr : int, outputDir : str):
    """
    Run the crew.
    """
    inputs = inputs

    #'aim': 'Calculate the Edelstein effect for a Kramers-Weyl fermion at the Gamma point of the Brillouin zone. ' #THIS IT THE FUTURE AIM FOR GETTING A MORE COMPLEX MODEL
         #   'Compute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field.'
          #  'Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity)',

    try:
        import os
        # set environment variables the runtime may read
        os.environ["CREWAI_ENABLE_AUTO_TOOL_CHOICE"] = "false"
        os.environ["CREWAI_TOOL_CALL_PARSER"] = "true"
        
        paperFinder = PaperFinderCrew(outputNr = outputNr, outputDir = outputDir)
        fullResult = paperFinder.crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

    return fullResult

def run_crew_modelling(inputs : dict, outputNr : int, outputDir : str):
    """
    Run the crew.
    """
    inputs = inputs

    #'aim': 'Calculate the Edelstein effect for a Kramers-Weyl fermion at the Gamma point of the Brillouin zone. ' #THIS IT THE FUTURE AIM FOR GETTING A MORE COMPLEX MODEL
         #   'Compute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field.'
          #  'Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity)',

    try:
        import os
        # set environment variables the runtime may read
        os.environ["CREWAI_ENABLE_AUTO_TOOL_CHOICE"] = "false"
        os.environ["CREWAI_TOOL_CALL_PARSER"] = "true"
        
        modelller = ModellerCrew(outputNr = outputNr, outputDir = outputDir)
        fullResult = modelller.crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

    return fullResult

def train(inputs : dict, outputNr : int, outputDir : str):
    """
    Train the crew for a given number of iterations.
    """
    inputs = inputs
    try:
        Physicsmodellinghelper(outputNr = outputNr, outputDir = outputDir).crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay(outputNr : int, outputDir : str):
    """
    Replay the crew execution from a specific task.
    """
    try:
        Physicsmodellinghelper(outputNr = outputNr, outputDir = outputDir).crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test(inputs : dict, outputNr : int, outputDir : str):
    """
    Test the crew execution and returns the results.
    """
    inputs = inputs

    try:
        Physicsmodellinghelper(outputNr = outputNr, outputDir = outputDir).crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger(inputs : dict, outputNr : int, outputDir : str):
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = inputs

    try:
        result = Physicsmodellinghelper(outputNr = outputNr, outputDir = outputDir).crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
