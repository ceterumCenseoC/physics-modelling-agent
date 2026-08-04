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
        aim = self.convert_messages_to_prompt(input)
        versionNr = getattr(config, "versionNr", 1)
        outputDir = getattr(config, "outputDir", "./evalOUTPUT/")
        temperature = getattr(config, "temperature", 1.0) # default values that don't modify anything
        top_p = getattr(config, "top_p", 1.0)
        max_tokens = getattr(config, "max_tokens", 100_000)
        max_iter = getattr(config, "max_iter", 3)
        reasoning = getattr(config, "reasoning", True)
        
        payload = json.dumps(
                                {
                                    "aim": aim,
                                    "versionNr": versionNr,
                                    "outputDir": outputDir,
                                    "temperature": temperature,
                                    "top_p": top_p,
                                    "max_tokens": max_tokens,
                                    "max_iter": max_iter,
                                    "reasoning": reasoning
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
