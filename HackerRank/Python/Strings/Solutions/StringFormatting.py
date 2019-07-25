def print_formatted(number):
    binary = '{0:b}'.format(number)
    width = len(binary)
    for i in range(1, number + 1):
        print('{0:{w}d} {0:{w}o} {0:{w}x} {0:{w}b}'.format(i, w=width).upper())

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)