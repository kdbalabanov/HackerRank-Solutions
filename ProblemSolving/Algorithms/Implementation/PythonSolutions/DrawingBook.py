#!/bin/python3

import os

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    from_beginning = p // 2
    from_end = n // 2 - p // 2
    return round(min(from_beginning, from_end))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    fptr.write(str(result) + '\n')
    fptr.close()