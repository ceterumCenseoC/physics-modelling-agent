from inspect_ai.model import ModelAPI, ModelOutput, ChatMessage, ToolInfo, ToolChoice, GenerateConfig
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
        return ModelOutput(choices=[{"text": resp["text"]}])