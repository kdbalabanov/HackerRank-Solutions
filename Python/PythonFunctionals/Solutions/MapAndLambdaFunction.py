cube = lambda x: x**3

def fibonacci(n):
    l = []
    for i in range(n):
        if len(l) < 2:
            l.append(i)
        else:
            l.append(l[-1] + l[-2])
    return l


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))