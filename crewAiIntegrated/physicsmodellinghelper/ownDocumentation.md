# inside the physicsmodellinghelper directory:
crewai run
# executes the main.py file located insite the src\physicsmodellinghelper directory

$trans = "..\crewRuns\session_$(Get-Date -Format yyyyMMdd_HHmmss).log"
Start-Transcript -Path $trans
crewai run
Stop-Transcript

# convert transcript to UTF-8 markdown
Get-Content $trans -Raw | Set-Content ..\crewRuns\session_$(Get-Date -Format yyyyMMdd_HHmmss).md -Encoding utf8
# for transcribing

# venv
# create venv
python -m venv .venv

# activate venv
.\.venv\Scripts\Activate.ps1

# install from requirements.txt
pip install -r requirements.txt

# used extension
Markdown Preview Enhanced
Yiyi Wang
# allows for good md view
# to enable markdown preview
STRG+SHIFT+V