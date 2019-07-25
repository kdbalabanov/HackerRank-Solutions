#!/bin/python3

import os

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max = None
    for i in range(len(arr[0]) - 2):
        for j in range(len(arr) - 2):
            current = sum(arr[j][i:i+3]) + arr[j+1][i+1] + sum(arr[j+2][i:i+3])
            if max is None or current > max:
                max = current
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()