_Explaination:
- CritPt module: is the repo from github used for the evaluation
- pma module provides the interface for CritPt to access the physics modelling assistant
  - structure is needed for it to be treated as a model
  - backend.py handles the interaction with the acctual physics modelling assistant
- pma_source is where the physics modelling assistant livies
  - has its seperate venv


_Virtual Environment setup for CritPt
# inside physic_modelling_assistant/CritPt
# create the virtual environment 
python -m venv .venv
# activate the virtual environment
./.venv/scripts/Activate.ps1
# install necessary packages
# the requirements of CritPt
pip install -r .\requirements.txt
# install all the content inside the CritPt dir to the venv # needs to be repeated if changes where made in the directory
pip install -e .
# the pma containing the physics modelling assistant's interface to CritPt; it needs to be installed into CritPt's venv # needs to be repeated if changes where made in the directory
pip install -e ../pma
# a .config is needed specifying hwo the model should be run
CritPt/.config/pma.json # is on git, so it will be there automatically

_setup for pma
# inside the pma
# needed to be recognised as a module
pyproject.toml

_setup for pma_source
# inside the pma_source
# needed to be recognised as a module
pyproject.toml
# handles the ineraction with pma
cli.py
# needs its own venv
python -m venv .venv
# activate the venv
.\.venv\Scripts\Activate.ps1
# install the requirements
pip install -r requirements.txt
# module needs to be installed into the active venv
pip install -e .


# run just the crew withoug CritPt
# activate the venv inside pma_source
./.venv/Scripts/Activate.ps1
# move out of the module
cd ..
# then run as a module
python -X utf8 -m pma_source.execute

# then run critpt (the __main__.py file in CritPt/src/critpt)
# from an active venv
python -m critpt generate generate model=pma/pma task_config=.config/pma.json
python -X utf8 -m critpt generate generate model=pma/pma task_config=.config/pmaAllChallanges.json

# run all generation challanges in sequence
# inside CritPt directory on an active venv
# windows
powershell -ExecutionPolicy Bypass -File .\runAllSequence.ps1
# linux: 1. make file executable: chmod +x runAllSequence.sh
chmod +x runAllSequence.sh
# linux: 2. run the script
./runAllSequence.sh

# establish the required format for the CritPt generations; works on results/generation
# run from the CritPt directory
python .\modifyOutputToMatchFormat.py

# run evaluation of the generated code
# inside CritPt directory on an active venv
python -m evaluate_all_results --api-key YOURAPIKEY --results-dir resultsNAME/generations

# for windows powershell, use the following command to check rate limits (linux command on GWDG webpage for SAIA):
- chat-ai.academiccloud.de
- saia.gwdg.de

curl.exe -i `
-H "Authorization: Bearer <API_KEY>" `
-H "Content-Type: application/json" `
"https://chat-ai.academiccloud.de/v1/chat/completions"#
HTTP/1.1 429 Too Many Requests
Date: Sun, 01 Aug 2026 09:02:28 GMT
Server: kong/3.6.1
Content-Type: application/json; charset=utf-8
RateLimit-Reset: 25052
Retry-After: 25052
X-RateLimit-Limit-Minute: 30
X-RateLimit-Limit-Hour: 200
X-RateLimit-Limit-Day: 1000
X-RateLimit-Limit-Month: 3000
RateLimit-Remaining: 0
RateLimit-Limit: 1000
X-RateLimit-Remaining-Minute: 30
X-RateLimit-Remaining-Hour: 200
X-RateLimit-Remaining-Day: 0
X-RateLimit-Remaining-Month: 1000
Content-Length: 92
X-Kong-Response-Latency: 1
X-Kong-Request-Id: 30000000000000000000000000000008
Access-Control-Allow-Origin: *

{
  "message":"API rate limit exceeded",
  "request_id":"30000000000000000000000000000008"
}
