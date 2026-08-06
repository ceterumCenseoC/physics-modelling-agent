# pma_provider/backend.py
import os
import sys
import json
import asyncio
from pathlib import Path
from inspect_ai.model import ModelAPI, ModelOutput, ChatMessage
import uuid

# Resolve pma_source subprocess path
class PMAModelAPI(ModelAPI):
    
    def convert_messages_to_prompt(self, messages: list[ChatMessage]) -> str: #check if this is correct for critpt
        parts = []
        for m in messages:
            role = getattr(m, "role", "user")
            text = getattr(m, "content", getattr(m, "text", ""))
            parts.append(f"{role}: {text}")
        return "\n".join(parts)

    def resolve_pma_paths(self) -> tuple[Path, Path]:
        repo_root = Path(__file__).resolve().parents[3]
        pma_root = repo_root

        if sys.platform == "win32":
            python_exe = pma_root / ".venv" / "Scripts" / "python.exe"
        else:
            python_exe = pma_root / ".venv" / "bin" / "python"

        cli_script = "pma_source.cli"
        return python_exe, cli_script, pma_root

    async def generate(self, input, tools, tool_choice, config):
        
        problem_id = getattr(config, "problem_id", str(uuid.uuid4()))  # Generate a unique problem_id if not provided
        aim = self.convert_messages_to_prompt(input)
        versionNr = getattr(config, "versionNr", 1)
        outputDir = getattr(config, "outputDir", "./evalOUTPUT/")
        temperature = getattr(config, "temperature", 1.0) # default values that don't modify anything
        top_p = getattr(config, "top_p", 0.95)
        max_tokens = getattr(config, "max_tokens", 50_000)
        max_iter = getattr(config, "max_iter", 3)
        reasoning = getattr(config, "reasoning", True)
        max_reasoning_attempts = getattr(config, "max_reasoning_attempts", 3)

        os.makedirs("." + outputDir, exist_ok=True)
        with open("." + outputDir + f"AIM{problem_id}.txt", "w", encoding="utf-8") as f:
            f.write(str(input) + "\n\n" + str(config)) # write the input messages and the converted aim to a file for debugging
        
        payload = json.dumps(
                                {
                                    "problem_id": problem_id,
                                    "aim": aim,
                                    "versionNr": versionNr,
                                    "outputDir": outputDir,
                                    "temperature": temperature,
                                    "top_p": top_p,
                                    "max_tokens": max_tokens,
                                    "max_iter": max_iter,
                                    "reasoning": reasoning,
                                    "max_reasoning_attempts": max_reasoning_attempts
                                }
                            )

        # location of the execution srcipts
        python_exe, cli_script, pma_root = self.resolve_pma_paths()

        # Spawn pma_source subprocess
        proc = await asyncio.create_subprocess_exec(
            str(python_exe),
            "-m", cli_script,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd = pma_root,
            text=False
        )

        # Send JSON payload
        stdout, stderr = await proc.communicate((payload + "\n").encode())

        text = ""
        os.makedirs("." + outputDir, exist_ok=True)
        with open("." + outputDir + f"output{problem_id}.txt", "r", encoding="utf-8") as f:
            text = f.read()
        
        if proc.returncode != 0:
            return ModelOutput.from_content( # see inspect_ai/model/_model_output.py for class definition of ModelOutput
                        model="pma-model",
                        content=f"failure: {stderr.decode()}"
                    ) 
        
        return ModelOutput.from_content( # see inspect_ai/model/_model_output.py for class definition of ModelOutput
            model="pma-model",
            content=text
        ) 

if __name__ == "__main__":
    # For testing purposes
    model_api = PMAModelAPI("pma_TEST")

    # Option A: If the library exposes concrete message classes, prefer them.
    # Try to import the concrete class; if not available, fall back to a simple shim.
    try:
        # adjust import path if the real names differ in your version
        from inspect_ai.model import ChatMessageUser  # or ChatMessageAssistant
        input_messages = [ChatMessageUser(content="Test aim for physics modelling.")]
    except Exception:
        # Fallback shim: a tiny object with the attributes your convert_messages_to_prompt expects
        class SimpleUserMsg:
            def __init__(self, content):
                self.role = "user"
                self.content = content
                self.text = content

        input_messages = [SimpleUserMsg("Test aim for physics modelling.")]

    # Build a simple config object or dict. The generate signature expects a GenerateConfig,
    # but your code uses getattr(config, "..."), so a simple object with attributes works.
    class SimpleConfig:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    config = SimpleConfig(
        versionNr=1
    )

    # generate() is async — run it properly
    import asyncio

    async def run_test():
        # tools and tool_choice can be None for this test
        result = await model_api.generate(input_messages, tools=None, tool_choice=None, config=config)
        # ModelOutput is a pydantic model; print a compact representation
        print("ModelOutput:", result)

    asyncio.run(run_test())

        