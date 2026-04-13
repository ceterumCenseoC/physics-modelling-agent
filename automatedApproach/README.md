# to see the idea of the project, run from the automatedApproach dir:
python -m exampleWorkflows.exampleWorkflow

# write output into a file:
python -X utf8 -m  exampleWorkflows.exampleWorkflows > logs/edelstein2.txt

# general structure
- src includes the files to access SAIA (and therefor the used LLM);
    the handling of the crewai objects Agent, Task, Crew
    an Orchestrator class that provides the interface to make a crew

- tests includes TESTS, rund the test with
python -m pytest .\tests\testCrewOrchestration.py

- preparedCrews dir includes a file containing methods that set up a concrete crew; the methods take a dict argument to pass the query the crew should work on to it

- problems dir includes a fle containing methods that define and return a dict; this dict defines a problem a crew can work on

- exampleWorkflows dir contains an executable file
    defines methods that feed a specific problem to a specific crew
    here preparedCrews and problems come together