$CONFIG = ".config/pma.json"

$myList = @(44)
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
# 50,52,68,69,70 worked on the second run
# 30,56 worked on the third run
# 44 failed again on the fifth try