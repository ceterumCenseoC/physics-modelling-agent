# crewai_service/cli.py
import sys
import json
from .execute import Physics_Modelling_Assistant

def main():
    try:
        data = json.load(sys.stdin)
        topic = data.get("topic", "") # string
        aim = data.get("aim", "") # string
        versionNr = data.get("versionNr", 1) # int
        outputDir = data.get("outputDir", "./critPt/eval/") # string
        temperature = data.get("temperature", 1.0) # float
        top_p = data.get("top_p", 1.0) # float

        # Import crewai inside isolated venv
        pma = Physics_Modelling_Assistant()
        text = pma.executeInterface(topic= topic,
                                    aim = aim, 
                                    outputDir = outputDir, 
                                    pdfSaveDir = "./critPt/eval/pdfs", 
                                    versionNr = versionNr, 
                                    temperature = temperature, 
                                    top_p = top_p)

        json.dump({"text": text}, sys.stdout)
        sys.stdout.flush()

    except Exception as e:
        print("ERROR:" + str(e), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
