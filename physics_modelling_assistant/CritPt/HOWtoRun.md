# in this directory (CritPt)
# activate the virtual environment
.venv/scripts/Activate.ps1

# then add CritPt contents so python interpreter sees them
pip install -e . # run this inside CritPt directory
# add a pth file pointing to the location of the own model that should be evaluated in CritPt/.venv/Lib/site-packages/agent_path.pth
# in this file write the relative location of your model from agent_path.pth
../../../../src

# then run critpt (the __main__.py file in CritPt/src/critpt)
python -m critpt generate generate model=pma/pma task_config=.config/pma.json