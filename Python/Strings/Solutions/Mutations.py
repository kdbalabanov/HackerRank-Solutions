def mutate_string(string, position, character):
    slist = list(string)
    slist[position] = character
    return ''.join(slist)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)