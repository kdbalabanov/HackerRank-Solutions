# Enter your code here. Read input from STDIN. Print output to STDOUT
tcases = int(input())
for i in range(tcases):
    na = int(input())
    A = set(input().split())
    nb = int(input())
    B = set(input().split())
    print(A.issubset(B)) 