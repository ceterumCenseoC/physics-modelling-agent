physics-modelling-agent
wants to help with physics

<!-- # testing the code directory
inside this directory:
source code/venv/bin/activate #activates the virtual environment
xvfb-run -a python code/src/connectAI.py # to run connectAI.py

use "xvfb-run -a" in front of python cmd to make webpage access possible
    only necessary on cocalc.gwdg.de (or other cloud service) 
xvfb-run -a python code/src/connectAI.py -->



# how to work locally is documented for each seperate subdirectory

# how to work on the remote server: https://cocalc.gwdg.de/projects
# it is linux based

# git
# pull from remote as usual:
git pull

# clone remote':
git clone https://github.com/ceterumCenseoC/physics-modelling-agent.

# push to git
git push



# create a .venv
mkdir .venv
cd .venv
python -m venv .

# activate the .venv
source .venv/bin/activate

# install from requirements.txt
pip install -r requirements.txt

# save current state into requirements.txt
pip freeze > requirements.txt


# on the remote, there is a path issue (the project root is defined differently), thatswhy a .sh script is used to run the crew
./run.sh


