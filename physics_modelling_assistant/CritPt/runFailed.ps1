$CONFIG = ".config/pma.json"

$myList = @(11,13,19,52,62,66,68,69,70) # needed for qwen2
foreach ($i in $myList) {

    Write-Host "Running challenge $i"

    # Read JSON
    $json = Get-Content $CONFIG | ConvertFrom-Json

    # Update challenge number
    $json.reader_paths[0] = "data/public_test_challenges/json/Challenge_$i.json"

    # Write JSON back
    $json | ConvertTo-Json -Depth 10 | Set-Content $CONFIG

    # Run command
    python -X utf8 -m critpt generate generate model=pma/pma task_config=$CONFIG
}
# failed DeepSeek1: 14,17,20,21,37 format issues
#failed Qwen1: 35,37,54 format issues
# failed Qwen2:
# 

# run DeepSeek2 from 1-6; and from 39-