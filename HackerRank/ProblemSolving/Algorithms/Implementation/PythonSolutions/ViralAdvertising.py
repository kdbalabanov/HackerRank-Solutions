#!/bin/python3

import os

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    liked = 2
    count = liked
    for i in range(1, n):
        liked = (liked * 3) // 2
        count += liked
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()