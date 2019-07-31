#!/bin/python3

import os

# Complete the findDigits function below.
def findDigits(n):
    count = 0
    l = list(map(int, list(str(n))))
    for num in l:
        if num != 0:
            if n % num == 0:
                count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = findDigits(n)
        fptr.write(str(result) + '\n')
    fptr.close()