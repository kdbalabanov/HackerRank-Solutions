# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as stat

n = int(input())
X = list(map(int, input().split()))
X.sort()
mid = len(X) // 2
quart_one = []
quart_two = int(stat.median(X))
quart_three = []

if len(X) % 2 == 0:
    quart_one = X[:mid]
    quart_three = X[mid:]
else:
    quart_one = X[:mid]
    quart_three = X[mid+1:]

print(int(stat.median(quart_one)))
print(quart_two)
print(int(stat.median(quart_three)))