# crewai_service/cli.py
import sys
import json
from .execute import Physics_Modelling_Assistant

def main(): # this works correctly
    ### Handles passing parameters to the physics modelling assistant during evaluation
    try:
        data = json.load(sys.stdin)

        problem_id = data.get("problem_id", "0")
        aim = data.get("aim", "no aim provided")
        versionNr = data.get("versionNr", 1)
        outputDir = data.get("outputDir", "./evalOUTPUT/")
        temperature = data.get("temperature", 1.0)
        top_p = data.get("top_p", 1.0)
        max_tokens = data.get("max_tokens", 50_000)
        max_iter = data.get("max_iter", 3)
        reasoning = data.get("reasoning", True)
        max_reasoning_attempts = data.get("max_reasoning_attempts", 3)

        pma = Physics_Modelling_Assistant()
        text = pma.executeInterfaceShortcut(# for test purposes: pma.executeInterfaceShortcut(; otherwise: pma.executeInterface(
            id = problem_id,
            aim=aim,
            outputDir=outputDir,
            pdfSaveDir=outputDir + "pdfs",
            versionNr=versionNr,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            max_iter=max_iter,
            reasoning=reasoning,
            max_reasoning_attempts=max_reasoning_attempts
        )
               
        import os
        print(outputDir)
        os.makedirs(outputDir, exist_ok=True)
        with open( outputDir + f"output{problem_id}.txt", "w", encoding="utf-8") as f:
            f.write(text)
        sys.stdout.flush() # signals to superprocess that output is complete and can be read
    except Exception as e:
        # Log human-readable error to stderr
        print("ERROR:" + str(e), file=sys.stderr)
        import os
        outputDir = "error_output/"
        if outputDir is not None:
            outputDir = "error_output/"
        os.makedirs( outputDir, exist_ok=True)
        with open( outputDir + f"output{problem_id}.txt", "w", encoding="utf-8") as f:
                    f.write(text)
        sys.stdout.flush()

if __name__ == "__main__":
    main()
