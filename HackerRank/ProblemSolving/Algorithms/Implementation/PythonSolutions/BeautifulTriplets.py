#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    s = set(arr)
    counter = 0
    
    for i in range(len(arr)):
        if arr[i] + d in s and arr[i] + 2 * d in s:
            counter += 1

    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    arr = list(map(int, input().rstrip().split()))
    result = beautifulTriplets(d, arr)
    fptr.write(str(result) + '\n')
    fptr.close()