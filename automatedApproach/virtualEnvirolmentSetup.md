# run the following commands to setup the virtual envirolment (venv) corretly; for WINDOWS

# create .venv directory
python -m venv venv

# first activate the venv; (Windows)
.\venv\Scripts\Activate.ps1
# or (Linux)
source venv/bin/activate

# then setup
pip install pip-tools #only first time
pip install pipreqs # only first time
pipreqs . --force --savepath requirements.in
pip-compile requirements.in

# pip-compile --upgrade # optional
pip install -r requirements.txt

# save the current pip state into the requirements file
pip freeze > requirements.txt
pip install -r requirements.txt