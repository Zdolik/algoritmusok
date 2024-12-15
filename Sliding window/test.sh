#!/bin/bash


echo "Teszt futtatása..."

test_cases=(
    "8 3\n2 4 3 5 8 1 2 1"
    "10 4\n1 2 3 4 5 6 7 8 9 10"
    "5 2\n10 20 10 30 10"
    "6 3\n1 1 1 1 1 1"
    "7 4\n3 7 2 5 8 6 4"
)

expected_outputs=(
    "2 2 5 7 7 1"
    "3 4 5 6 7 8"
    "10 10 20 20"
    "0 0 0 0"
    "9 10 15 16"
)

for i in "${!test_cases[@]}"; do
    echo -e "Teszt #$((i+1))"
    echo -e "${test_cases[i]}" | python3 solution.py > output.txt
    result=$(<output.txt)
    echo "Eredmény: $result"
    echo "Elvárt: ${expected_outputs[i]}"
    if [ "$result" == "${expected_outputs[i]}" ]; then
        echo "Sikeres teszt!"
    else
        echo "Sikertelen teszt!"
    fi
    echo "---------------------"
done