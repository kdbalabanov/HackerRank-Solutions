#!/bin/python3

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_locations = [x for x in [j + a for j in apples] if s <= x <= t]
    oranges_locations = [x for x in [j + b for j in oranges] if s <= x <= t]
    print(len(apples_locations))
    print(len(oranges_locations))

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
