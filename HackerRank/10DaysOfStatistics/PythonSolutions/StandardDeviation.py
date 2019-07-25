# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as stat

n = int(input())
X = list(map(int, input().split()))
print(stat.pstdev(X))