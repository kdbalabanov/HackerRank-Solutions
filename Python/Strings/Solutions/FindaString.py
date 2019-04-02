def count_substring(string, sub_string):
    count = 0
    j = 0
    for i in range(0, len(string)):
        index = string.find(sub_string, j, len(string))
        if index > -1:
            count += 1
            j += index + 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)