#!/bin/python3

import os
import sys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()