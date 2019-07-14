#!/bin/python3

import os

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    side_len = len(s) // 2
    l = [ord(x) for x in s]
    first_half = l[:side_len]
    second_half = l[-side_len:]
    second_half.reverse()
    count = 0
    for (x, y) in zip(first_half, second_half):
        if x < y:
            while x < y:
                y -= 1
                count += 1
        if x > y:
            while x > y:
                x -= 1
                count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = theLoveLetterMystery(s)
        fptr.write(str(result) + '\n')
    fptr.close()