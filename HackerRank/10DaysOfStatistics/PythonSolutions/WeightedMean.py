# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
xlist = list(map(int, input().split()))
wlist = list(map(int, input().split()))
print(round(sum([x * w for (x, w) in zip(xlist, wlist)]) / sum(wlist), 1))