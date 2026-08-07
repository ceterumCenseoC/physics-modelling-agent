import subprocess
import json

CONFIG = ".config/pma.json"

for i in range(1, 71):
    print(f"Running challenge {i}")

    # Load JSON
    with open(CONFIG, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Update challenge number
    data["reader_paths"][0] = f"data/public_test_challenges/json/Challenge_{i}.json"

    # Save JSON
    with open(CONFIG, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    # Run your command
    cmd = [
        "python",
        "-X", "utf8",
        "-m", "critpt",
        "generate",
        "generate",
        "model=pma/pma",
        f"task_config={CONFIG}"
    ]

    subprocess.run(cmd, check=True)
