#!/bin/python3

import os
from collections import Counter

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    counter_s1 = Counter(s1)
    counter_s2 = Counter(s2)
    return sum((counter_s1-counter_s2).values())+sum((counter_s2-counter_s1).values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = makingAnagrams(s1, s2)
    fptr.write(str(result) + '\n')
    fptr.close()
