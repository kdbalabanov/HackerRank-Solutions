#!/bin/python3

import os

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(k, ar):
    l = [x for indx, x in enumerate(ar) for indj, j in enumerate(ar) if indx != indj and (x + j) % k == 0]
    return round(len(l)/2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    k = int(nk[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(k, ar)
    fptr.write(str(result) + '\n')
    fptr.close()