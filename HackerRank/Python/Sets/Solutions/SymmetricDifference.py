# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
ms = set(map(int, input().split()))
n = int(input())
ns = set(map(int, input().split()))

s = ms.difference(ns).union(ns.difference(ms))
for x in sorted(s):
    print(x)