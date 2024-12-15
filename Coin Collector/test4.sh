#!/bin/bash

TEST_CASES=("4 4
4 5 2 7
1 2
2 1
1 3
2 4" 
"3 2
1 2 3
1 2
2 3" 
"5 5
10 20 30 40 50
1 2
2 3
3 4
4 5
5 1")

EXPECTED_OUTPUTS=("16" "6" "150")

echo "=== MAXIMUM ÉRMEGYŰJTÉS TESZT ==="
for i in "${!TEST_CASES[@]}"; do
    echo "Teszt #$((i+1)):"
    echo "${TEST_CASES[$i]}" | python3 solution.py > output.txt
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