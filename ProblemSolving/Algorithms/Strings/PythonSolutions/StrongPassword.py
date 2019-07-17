#!/bin/python3

import os

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    p = set(password)
    numbers = set("0123456789")
    lower_case = set("abcdefghijklmnopqrstuvwxyz")
    upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = set("!@#$%^&*()-+")
    count = 0 
    if p.isdisjoint(numbers):
        count += 1
    if p.isdisjoint(lower_case):
        count += 1
    if p.isdisjoint(upper_case):
        count += 1
    if p.isdisjoint(special_characters):
        count += 1
    if n + count < 6:
        count += (6 - (n + count))
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    password = input()
    answer = minimumNumber(n, password)
    fptr.write(str(answer) + '\n')
    fptr.close()