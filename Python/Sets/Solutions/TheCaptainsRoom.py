import collections

# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
l = list(map(int, input().split()))
groups = round(len(l)/K)
counter = collections.Counter(l)
print(counter.most_common()[-1][0])