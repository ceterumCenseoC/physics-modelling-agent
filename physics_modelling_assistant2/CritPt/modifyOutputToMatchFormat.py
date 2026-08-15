import json

from anyio import Path

def replace(generated_code : str) -> str:
    """
    Replaces occurrences of 'python' with 'Python' in the generated code.

    Args:
        generated_code (str): The generated code to be modified.

    Returns:
        str: The modified generated code with 'python' replaced by 'Python'.
    """
    generated_code = generated_code.replace("```python\n", "").replace("```", "")
    return generated_code

def remove_non_python(path : str) -> None:
    """
    Removes all non-Python files from the specified directory.

    Args:
        path (str): The path to the directory from which to remove non-Python files.
    """
    from pathlib import Path

    root = Path(path)

    for file in root.rglob("Challenge_*_main.json"):
        # Read the JSON content
        print(f"Processing file: {file}")
        data = json.loads(file.read_text())

        # Check if the structure exists
        if "generated_code" in data and len(data["generated_code"]) > 0:
            data["generated_code"] = replace(data["generated_code"])

        if "messages" in data and len(data["messages"]) > 0:
            messages = data["messages"]
            # Check if the first message is from the user
            if "content" in messages[0]:
                messages[0]["content"] = replace(messages[0]["content"])  # If the content does not contain "python", remove the file

        json.dump(data, file.open("w"), indent=2)  # Write the modified JSON back to the file

if __name__ == "__main__":
    # Example usage: remove non-Python files from the 'output' directory
    remove_non_python("./results/generations/")