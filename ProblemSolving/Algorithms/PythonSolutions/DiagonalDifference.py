#!/bin/python3

import os

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def diagonalDifference(arr):
    # Write your code here
    length = len(arr)
    a = 0
    b = 0
    
    for i in range(0, length, 1):
        a += arr[i][i]
        b += arr[i][length - 1 - i]
        
    return abs(a - b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()