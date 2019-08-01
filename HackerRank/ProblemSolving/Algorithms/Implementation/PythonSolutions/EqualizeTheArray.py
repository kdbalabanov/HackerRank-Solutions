#!/bin/python3

import os
from collections import Counter 

# Complete the equalizeArray function below.
def equalizeArray(arr):
    counter = Counter(arr)
    return len(arr) - max(counter.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)
    fptr.write(str(result) + '\n')
    fptr.close()