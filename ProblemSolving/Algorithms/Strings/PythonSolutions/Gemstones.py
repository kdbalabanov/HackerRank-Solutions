#!/bin/python3

import os

# Complete the gemstones function below.
def gemstones(arr):
    l = [set(x) for x in arr]
    s = set.intersection(*l)
    return len(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = gemstones(arr)
    fptr.write(str(result) + '\n')
    fptr.close()