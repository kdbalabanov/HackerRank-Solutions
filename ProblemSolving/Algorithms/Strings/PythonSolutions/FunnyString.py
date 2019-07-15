#!/bin/python3

import os

# Complete the funnyString function below.
def funnyString(s):
    sl = [ord(x) for x in s]
    slr = sl[::-1]
    sl_diff = [abs(x - sl[indx + 1]) for indx, x in enumerate(sl) if indx + 1 < len(sl)]
    slr_diff = [abs(x - slr[indx + 1]) for indx, x in enumerate(slr) if indx + 1 < len(slr)]
    if sl_diff == slr_diff:
        return 'Funny'
    else:
        return 'Not Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        fptr.write(result + '\n')
    fptr.close()