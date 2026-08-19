import json

from anyio import Path

def replacing(generated_code : str) -> str:
    """
    Replaces occurrences of 'python' with 'Python' in the generated code.

    Args:
        generated_code (str): The generated code to be modified.

    Returns:
        str: The modified generated code with 'python' replaced by 'Python'.
    """
    generated_code = generated_code.replace("```python\n", "").replace("```", "")
    if "import sympy as sp" in generated_code:
        generated_code = "import sympy as sp" + generated_code.split("import sympy as sp", 1)[1]
    elif "def answer(" in generated_code:
        generated_code = "def answer(" + generated_code.split("def answer(", 1)[1]
    else:
        pass
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
            data["generated_code"] = replacing(data["generated_code"])

        # this is not necessary for the benchmarking
        """ if "messages" in data and len(data["messages"]) > 0:
            messages = data["messages"]
            # Check if the first message is from the user
            if "content" in messages[0]:
                messages[0]["content"] = replacing(messages[0]["content"])  # If the content does not contain "python", remove the file """

        json.dump(data, file.open("w"), indent=2)  # Write the modified JSON back to the file

if __name__ == "__main__":
    # Example usage: remove non-Pythonic files from the 'results' directory
    remove_non_python("./results/generations/")