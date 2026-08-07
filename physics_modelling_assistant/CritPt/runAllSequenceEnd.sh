#!/bin/bash

CONFIG=".config/pma.json"

for i in $(seq 70 1); do
    echo "Running challenge $i"

    sed -i "s|Challenge_[0-9]\+\.json|Challenge_${i}.json|" "$CONFIG"

    python -X utf8 -m critpt generate generate model=pma/pma task_config=$CONFIG
done
