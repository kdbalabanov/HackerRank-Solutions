# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median

n = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))
S = [x for x, y in zip(X, F) for _ in range(y)]
S.sort()
mid = len(S) // 2
quart_one = []
quart_three = []

if len(S) % 2 == 0:
    quart_one = S[:mid]
    quart_three = S[mid:]
else:
    quart_one = S[:mid]
    quart_three = S[mid+1:]

print(float(median(quart_three) - median(quart_one)))