#!/bin/python3

import os
from collections import Counter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    freq = Counter(arr)
    m = max(freq.values())
    l = [x for x, y in freq.items() if y == m]
    return min(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()