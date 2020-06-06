import numpy

def arrays(arr):
    return numpy.array(list(map(float, arr[::-1])))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)