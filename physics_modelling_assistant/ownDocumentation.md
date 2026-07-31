# from the physics_modelling_assistant directory
# run the full system as a module with
pyhton -m src.execute #-m tells the interpreter to treat src as a package allowing for relative imports

# venv
# create venv
python -m venv .venv

# activate venv
.\.venv\Scripts\Activate.ps1

# install from requirements.txt
pip install -r requirements.txt

# save .venv settings to requirements.txt
pip freeze > .\requirements.txt


# used extension
Markdown Preview Enhanced
Yiyi Wang
# allows for good md view
# to enable markdown preview
STRG+SHIFT+V