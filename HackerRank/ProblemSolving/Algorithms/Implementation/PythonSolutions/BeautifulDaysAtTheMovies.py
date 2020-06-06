import math
import os
import random
import re
import sys


def reverseNumber(num):
    reversedListOfChars = list(str(num))
    reversedListOfChars.reverse()
    return int("".join(reversedListOfChars))

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    counter = 0
    
    for day in range(i, j + 1):
        reversedNum = reverseNumber(day)
        difference = abs(day-reversedNum)

        if difference % k == 0:
            counter += 1
    
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ijk = input().split()
    i = int(ijk[0])
    j = int(ijk[1])
    k = int(ijk[2])
    result = beautifulDays(i, j, k)
    fptr.write(str(result) + '\n')
    fptr.close()