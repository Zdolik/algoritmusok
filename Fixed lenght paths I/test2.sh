#!/bin/bash

echo "Rekurziós teszt futtatása..."

test_cases=(
    "5 2\n1 2\n2 3\n3 4\n3 5"
    "4 1\n1 2\n2 3\n3 4"
    "6 3\n1 2\n2 3\n3 4\n4 5\n5 6"
    "3 2\n1 2\n2 3"
    "7 2\n1 2\n1 3\n2 4\n2 5\n3 6\n3 7"
)

expected_outputs=(
    "4"
    "3"
    "4"
    "2"
    "6"
)

for i in "${!test_cases[@]}"; do
    echo -e "Teszt #$((i+1))"
    echo -e "${test_cases[i]}" | python3 solution.py > output.txt
    result=$(<output.txt)
    echo "Eredmény: $result"
    echo "Elvárt: ${expected_outputs[i]}"
    if [ "$result" == "${expected_outputs[i]}" ]; then
        echo "Sikeres teszt!"
    elses
        echo "Sikertelen teszt!"
    fi
    echo "---------------------"
done