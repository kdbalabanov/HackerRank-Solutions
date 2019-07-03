#!/bin/python3

import os

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level = 0
    current_level = 0
    valleys = 0
    valley_detected = False

    for step in s:
        if step == 'D':
            current_level -= 1
        elif step == 'U':
            current_level += 1

        if current_level < sea_level and not valley_detected:
            valleys += 1
            valley_detected = True
        elif current_level == sea_level:
            valley_detected = False
    
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()