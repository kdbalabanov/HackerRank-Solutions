# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
N = set(input().split())
m = int(input())
M = set(input().split())
print(len(N.difference(M)))