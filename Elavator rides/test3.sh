#!/bin/bash

TEST_CASES=("4 10
4 8 6 1" "5 15
2 3 7 8 4" "3 5
2 2 2" "1 100
99")

EXPECTED_OUTPUTS=("2" "3" "2" "1")

echo "=== LIFTOPTIMALIZÁCIÓS TESZT ==="
for i in "${!TEST_CASES[@]}"; do
    echo "Teszt #$((i+1)):"
    echo "${TEST_CASES[$i]}" | python3 feladat3.py > output.txt
    OUTPUT=$(cat output.txt)

    if [ "$OUTPUT" == "${EXPECTED_OUTPUTS[$i]}" ]; then
        echo "Sikeres teszt!"
    else
        echo "Sikertelen teszt!"
        echo "Elvárt: ${EXPECTED_OUTPUTS[$i]}"
        echo "Kapott: $OUTPUT"
    fi
    echo "-----------------------"
done