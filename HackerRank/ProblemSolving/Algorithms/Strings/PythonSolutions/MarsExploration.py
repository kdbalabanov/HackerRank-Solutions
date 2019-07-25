#!/bin/python3

import os

# Complete the marsExploration function below.
def marsExploration(s):
    length = len(s)
    multiple = round(length / 3)
    actual = 'SOS' * multiple
    return len([x for indx, x in enumerate(actual) if x != s[indx]])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = marsExploration(s)
    fptr.write(str(result) + '\n')
    fptr.close()