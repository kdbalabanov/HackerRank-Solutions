#!/bin/python3

import os

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    hr = 'hackerrank'
    count = 0
    for i in range(0, len(s)):
        if count < len(hr) and s[i] == hr[count]:
            count += 1
    if count == len(hr):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = hackerrankInString(s)
        fptr.write(result + '\n')
    fptr.close()