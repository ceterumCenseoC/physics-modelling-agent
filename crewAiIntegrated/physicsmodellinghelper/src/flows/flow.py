from crewai.flow import Flow, start, listen
from crewai.flow.persistence import persist
from pydantic import BaseModel
from flows.main import run_crew_paperFinder, run_crew_modelling

class CounterState(BaseModel):
    id: str = ""
    counter: int = 0
    data: dict = {}

@persist()
class CounterFlow(Flow[CounterState]):

    @start()
    def paperFinding(self):
        result = run_crew_paperFinder(
            inputs=self.state.data["inputs"],
            outputNr=self.state.data["outputNr"],
            outputDir=self.state.data["outputDir"]
        )
        self.state.data["previous_output"] = result
        self.state.counter += 1

    @listen(paperFinding)
    def modelling(self):
        result = run_crew_modelling(
            inputs=self.state.data["inputs"],
            previous_output=self.state.data["previous_output"],
            outputNr=self.state.data["outputNr"],
            outputDir=self.state.data["outputDir"]
        )
        self.state.data["model_result"] = result
        self.state.counter += 1


if __name__ == "__main__":
    outputNr = 1
    outputDir = "runOutputsFLOWS/"

    initial_state = CounterState(
        id="run1",
        counter=0,
        data={
            "inputs": {
                'topic': 'Edelstein-Effect',
                'aim': (
                    'Calculate the Edelstein effect for a Rashba fermion (at the Gamma point of the Brillouin zone). '
                    'Compute the magnitization magnitude and direction for different directions and magnitudes of the applied electric field. '
                    'Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity, '
                    'spin-orbit coupling strength) and make explicit graphics.'
                ),
                'previous_output': None
            },
            "outputNr": outputNr,
            "outputDir": outputDir
        }
    )

    # Run only paperFinding
    flow_1 = CounterFlow(target = CounterFlow)
    state_after_step1 = flow_1.kickoff(until="paperFinding", initial_state=initial_state)

    # Later: run only modelling, using saved state
    flow_2 = CounterFlow(initial_state)
    state_after_step2 = flow_2.kickoff(until="modelling", initial_state=state_after_step1)
