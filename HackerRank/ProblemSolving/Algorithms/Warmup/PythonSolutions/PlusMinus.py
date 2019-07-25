#!/bin/python3

# Complete the plusMinus function below.
def plusMinus(arr, n):
    positives = 0
    negatives = 0
    zeros = 0

    for num in arr:
        if num > 0:
            positives += 1
        elif num < 0:
            negatives += 1
        else:
            zeros +=1
    
    print(str.format('{0:.6f}', positives/n))
    print(str.format('{0:.6f}', negatives/n))
    print(str.format('{0:.6f}', zeros/n))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr, n)