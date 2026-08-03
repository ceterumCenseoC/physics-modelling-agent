_Virtual Environment setupt
# inside physic_modelling_assistant/CritPt
# create the virtual environment 
python -m venv .venv
# activate the virtual environment
.venv/scripts/Activate.ps1
# install necessary packages
# the requirements of CritPt
pip install -r .\requirements.txt
# the pma containing the physics modelling assistant's interface to CritPt; it needs to be installed into CritPt's venv
pip install -e ../pma

_Explaination:
- CritPt module: is the repo from github used for the evaluation
- pma module provides the interface for CritPt to access the physics modelling assistant
  - structure is needed for it to be treated as a model
  - backend.py handles the interaction with the acctual physics modelling assistant
- pma_source is where the physics modelling assistant livies
  - has its seperate venv

# then run critpt (the __main__.py file in CritPt/src/critpt)
python -m critpt generate generate model=pma/pma task_config=.config/pma.json