# run the following commands to setup the virtual envirolment (venv) corretly; for WINDOWS

# first activate the venv
.\venv\Scripts\Activate.ps1

# then setup
pip install pip-tools # only first time
pip-compile requirements.in

# pip-compile --upgrade # optional
pip install -r requirements.txt

# save the current pip state into the requirements file
pip freeze > requirements.txt
pip install -r requirements.txt