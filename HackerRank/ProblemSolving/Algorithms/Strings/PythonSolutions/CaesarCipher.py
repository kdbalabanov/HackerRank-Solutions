#!/bin/python3

import os

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    l = []
    for x in s:
        num = ord(x)
        if 97 <= num <= 122:
            l.append(chr(((num-97+k)%26)+97))
        elif 65 <= num <= 90:
            l.append(chr(((num-65+k)%26)+65))
        else:
            l.append(x)
    return ''.join(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    k = int(input())
    result = caesarCipher(s, k)
    fptr.write(result + '\n')
    fptr.close()