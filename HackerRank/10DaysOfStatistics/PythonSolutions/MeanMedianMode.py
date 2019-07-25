# Enter your code here. Read input from STDIN. Print output to STDOUT
from scipy import stats
import statistics as stat

N = int(input())
ints = list(map(int, input().split()))
print(stat.mean(ints))
print(stat.median(ints))
print(int(stats.mode(ints)[0]))