import os
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = Counter(ar)
    pairs = 0

    for pair in count.values():
        pairs += pair // 2
    
    return round(pairs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()