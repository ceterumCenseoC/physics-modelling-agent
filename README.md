physics-modelling-agent
wants to help with physics

# testing the code directory
inside this directory:
source code/venv/bin/activate #activates the virtual environment
xvfb-run -a python code/src/connectAI.py # to run connectAI.py

use "xvfb-run -a" in front of python cmd to make webpage access possible
    only necessary on cocalc.gwdg.de (or other cloud service) 
xvfb-run -a python code/src/connectAI.py

