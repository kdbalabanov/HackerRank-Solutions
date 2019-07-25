# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
n = int(input())
result = True
for i in range(n):
    s = set(input().split())
    if not A.issuperset(s):
        result = False
print(result)