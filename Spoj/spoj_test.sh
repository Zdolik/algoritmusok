#!/bin/bash

chmod +x solution.py

echo "Running test cases..."

echo -e "5 7\n5 2 100\n3 5 80\n2 3 70\n2 1 50\n3 4 90\n4 1 85\n3 1 70\n0" | python3 spoj.py > output1.txt
EXPECTED1="61.200000 percent"
OUTPUT1=$(cat output1.txt)

if [ "$OUTPUT1" == "$EXPECTED1" ]; then
    echo "Test Case 1 Passed"
else
    echo "Test Case 1 Failed: Expected '$EXPECTED1' but got '$OUTPUT1'"
fi
