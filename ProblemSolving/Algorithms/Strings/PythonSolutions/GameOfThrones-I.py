#!/bin/python3

import os

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    l = []
    for c in set(s):
        l.append(s.count(c))
    odd_counts = len([x for x in l if x % 2 != 0])
    if odd_counts > 1:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = gameOfThrones(s)
    fptr.write(result + '\n')
    fptr.close()