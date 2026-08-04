# crewai_service/cli.py
import sys
import json
from .execute import Physics_Modelling_Assistant

def main():
    ### Handles passing parameters to the physics modelling assistant during evaluation
    try:
        data = json.load(sys.stdin)
        aim = data.get("aim", "") # string
        versionNr = data.get("versionNr", 1) # int
        outputDir = data.get("outputDir", "./critPt/eval/") # string
        temperature = data.get("temperature", 1.0) # float
        top_p = data.get("top_p", 1.0) # float
        max_tokens = data.get("max_tokens", 100_000) # int
        max_iter = data.get("max_iter", 3) # int
        reasoning = data.get("reasoning", True) # bool

        # Import crewai inside isolated venv
        pma = Physics_Modelling_Assistant()
        text = pma.executeInterface(aim = aim,
                                    outputDir = outputDir, 
                                    pdfSaveDir = outputDir + "pdfs", 
                                    versionNr = versionNr, 
                                    temperature = temperature, 
                                    top_p = top_p, 
                                    max_tokens = max_tokens,
                                    max_iter = max_iter,
                                    reasoning = reasoning)

        json.dump({"text": text}, sys.stdout)
        sys.stdout.flush()

    except Exception as e:
        print("ERROR:" + str(e), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
