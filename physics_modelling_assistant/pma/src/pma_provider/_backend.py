""" from inspect_ai.model import ModelAPI, ModelOutput, ChatMessage, ToolInfo, ToolChoice, GenerateConfig
import json, subprocess, sys

class CritPtExposeAPI(ModelAPI):
    __registry_name__ = "pma"  # This is the name that will be used to register the model in the registry   
    def __init__(self, model_name: str, **model_args):
        super().__init__(model_name, **model_args)

    async def generate(self, input, tools=None, tool_choice = None, config=None, cache=None) -> ModelOutput:
        # latest user message
        user_input = input[-1].content

        # run your agent pipeline
        output = await self.agent.executeInterface(topic="", aim=user_input, outputDir="./critPt/eval/", pdfSaveDir="./critPt/eval/pdfs", versionNr=1)

        # return Inspect-compatible output
        # investigate how this object really works
        return ModelOutput(choices=[ToolChoice(message=ChatMessage(role="assistant", content=output))])
        return {
            "role": "assistant",
            "content": output
        }

    async def generate(self, input, tools, tool_choice, config):
        proc = subprocess.Popen(
            ["./crewai_service/.venv/bin/python", "crewai_service/cli.py"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        inp = json.dumps({"prompt": input[-1].content})
        out, err = proc.communicate(inp, timeout=30)
        if proc.returncode != 0:
            raise RuntimeError(f"physics modelling assistant subprocess failed: {err}")
        resp = json.loads(out)
        return ModelOutput(choices=[{"text": resp["text"]}]) """

# pma_provider/backend.py
import sys
import json
import asyncio
from pathlib import Path
from inspect_ai.model import ModelAPI, ModelOutput, ChatMessage

# Resolve pma_source subprocess path
class PMAModelAPI(ModelAPI):
    def convert_messages_to_prompt(self, messages: list[ChatMessage]) -> str:
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
        prompt = self.convert_messages_to_prompt(input)
        temperature = getattr(config, "temperature", 1.0) # default values that don't modify anything
        top_p = getattr(config, "top_p", 1.0)
        max_tokens = getattr(config, "max_tokens", 250_000)
        payload = json.dumps(
                                {
                                    "prompt": prompt,
                                    "temperature": temperature,
                                    "top_p": top_p,
                                    "max_tokens": max_tokens,
                                    "versionNr": 1,
                                    "outputDir": "./critPt/eval/"
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

        if proc.returncode != 0:
            raise RuntimeError(stderr.decode())

        resp = json.loads(stdout.decode())
        text = resp.get("text", "")

        return ModelOutput(choices=[{"text": text}])
