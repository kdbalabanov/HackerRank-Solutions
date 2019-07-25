#!/bin/python3

import os

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    s = list(s)
    count = 0
    for i in range(0, len(s)):
        if i + 1 < len(s):
            if s[i] == s[i+1]:
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        fptr.write(str(result) + '\n')
    fptr.close()