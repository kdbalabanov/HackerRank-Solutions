#!/bin/python3

import os

# Complete the camelcase function below.
def camelcase(s):
    return len([x for x in s if x.isupper()]) + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = camelcase(s)
    fptr.write(str(result) + '\n')
    fptr.close()