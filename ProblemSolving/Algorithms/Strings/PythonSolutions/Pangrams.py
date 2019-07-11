#!/bin/python3

import os
import string

# Complete the pangrams function below.
def pangrams(s):
    alphabet = set(string.ascii_lowercase)
    if set(s.lower()) >= alphabet:
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = pangrams(s)
    fptr.write(result + '\n')
    fptr.close()