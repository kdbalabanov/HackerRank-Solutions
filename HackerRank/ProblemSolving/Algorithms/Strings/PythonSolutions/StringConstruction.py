#!/bin/python3

import os

# Complete the stringConstruction function below.
def stringConstruction(s):
    result = ''
    cost = 0
    for c in s:
        if c not in result:
            cost += 1
        result += c
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = stringConstruction(s)
        fptr.write(str(result) + '\n')
    fptr.close()
