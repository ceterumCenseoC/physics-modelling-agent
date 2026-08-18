$CONFIG = ".config/pma.json"

for ($i = 23; $i -le 70; $i++) {
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
# none