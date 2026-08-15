$CONFIG = ".config/pma.json"

$myList = @(9,10,11,13,22)
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
