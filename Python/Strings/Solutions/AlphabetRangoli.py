from string import ascii_lowercase

def print_rangoli(size):
    alphabet = list(ascii_lowercase)[:size]
    alphabet.reverse()
    max_row_len = 2 * len('-'.join(alphabet)) - 1
    max_row_num = 2 * size - 1
    row_counter = 0
    i = 1
    increment = 1
    while row_counter < max_row_num:
        l = alphabet[0:i]
        l = l[i:] + l[::-1]
        l = l[::-1] + l[1:]
        s = '-'.join(map(str, l))
        print(s.center(max_row_len, '-'))
        if len(s) == max_row_len:
            increment = -1    
        i += increment
        row_counter += 1