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