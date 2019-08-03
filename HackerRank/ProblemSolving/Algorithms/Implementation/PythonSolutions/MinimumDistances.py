#!/bin/python3

import os

# Complete the minimumDistances function below.
def minimumDistances(a):
    subs = []
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                subs.append(abs(i - j))
    if not subs:
        return -1
    return min(subs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)
    fptr.write(str(result) + '\n')
    fptr.close()