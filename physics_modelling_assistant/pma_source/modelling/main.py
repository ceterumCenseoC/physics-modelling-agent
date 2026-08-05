#!/usr/bin/env python
import sys
import warnings

from .crew_modelling import ModellerCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run_crew_modelling(inputs : dict, outputDir : str, pdfSaveDir : str, temperature: float, top_p: float, max_tokens: int, max_iter: int, reasoning : bool, max_reasoning_attempts: int):
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
        
        # crew, agent, task initialization, nothing too special, defines sync or async execution
        modeller = ModellerCrew(outputDir = outputDir, pdfSaveDir = pdfSaveDir, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = reasoning, max_reasoning_attempts = max_reasoning_attempts)
        # run the crew
        fullResult = modeller.crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

    return fullResult

def train(inputs : dict, outputDir : str, pdfSaveDir : str, temperature: float, top_p: float, max_tokens: int, max_iter: int, reasoning : bool, max_reasoning_attempts: int):
    """
    Train the crew for a given number of iterations.
    """
    inputs = inputs
    try:
        ModellerCrew(outputDir = outputDir, pdfSaveDir = pdfSaveDir, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = reasoning, max_reasoning_attempts = max_reasoning_attempts).crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay(outputDir : str, pdfSaveDir : str, temperature: float, top_p: float, max_tokens: int, max_iter: int, reasoning : bool, max_reasoning_attempts: int):
    """
    Replay the crew execution from a specific task.
    """
    try:
        ModellerCrew(outputDir = outputDir, pdfSaveDir = pdfSaveDir, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = reasoning, max_reasoning_attempts = max_reasoning_attempts).crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test(inputs : dict, outputDir : str, pdfSaveDir : str, temperature: float, top_p: float, max_tokens: int, max_iter: int, reasoning : bool, max_reasoning_attempts: int):
    """
    Test the crew execution and returns the results.
    """
    inputs = inputs

    try:
        ModellerCrew(outputDir = outputDir, pdfSaveDir = pdfSaveDir, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = reasoning, max_reasoning_attempts = max_reasoning_attempts).crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger(inputs : dict, outputDir : str, pdfSaveDir : str, temperature: float, top_p: float, max_tokens: int, max_iter: int, reasoning : bool, max_reasoning_attempts: int):
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
        result = ModellerCrew(outputDir = outputDir, pdfSaveDir = pdfSaveDir, temperature = temperature, top_p = top_p, max_tokens = max_tokens, max_iter = max_iter, reasoning = reasoning, max_reasoning_attempts = max_reasoning_attempts).crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
