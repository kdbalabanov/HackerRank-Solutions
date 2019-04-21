# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    user_in = input().split()
    op = user_in[0]
    ns = set(map(int, input().split()))
    exec('s.' + op + '(ns)')
print(sum(s))