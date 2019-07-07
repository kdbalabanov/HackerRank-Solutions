#!/bin/python3

import os

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    catA_pos = abs(x - z)
    catB_pos = abs(y - z)

    if catA_pos == catB_pos:
        return "Mouse C"
    elif catA_pos < catB_pos:
        return "Cat A"
    elif catB_pos < catA_pos:
        return "Cat B" 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
        fptr.write(result + '\n')

    fptr.close()
