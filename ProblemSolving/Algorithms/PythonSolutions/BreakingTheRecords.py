#!/bin/python3

import os

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highScore = lowScore = scores[0]
    highCount = lowCount = 0

    for score in scores:
        if highScore < score:
            highScore = score
            highCount += 1
        if lowScore > score:
            lowScore = score
            lowCount += 1

    return (highCount, lowCount) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()