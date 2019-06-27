#!/bin/python3

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    results = []
    
    for i in range(0, len(arr)):
        result = sum([x for index, x in enumerate(arr) if index != i])
        results.append(result)
    
    print(min(results), max(results))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)