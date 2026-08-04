# crewai_service/cli.py
import sys
import json
from .execute import Physics_Modelling_Assistant

def main():
    try:
        data = json.load(sys.stdin)
        prompt = data.get("prompt", "")

        # Import crewai inside isolated venv
        pma = Physics_Modelling_Assistant()
        text = pma.executeInterface(topic="", aim=prompt, outputDir="./critPt/eval/", pdfSaveDir="./critPt/eval/pdfs", versionNr=1)

        json.dump({"text": text}, sys.stdout)
        sys.stdout.flush()

    except Exception as e:
        print("ERROR:" + str(e), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
