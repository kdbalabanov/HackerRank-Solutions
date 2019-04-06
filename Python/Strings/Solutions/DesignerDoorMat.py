user_input = input().split()
height = int(user_input[0])
width = int(user_input[1])
element = '.|.'
center = 'WELCOME'
element_counter = 1
increment = 2

for i in range(height):
    l = []
    for i in range(element_counter):
        l.append(element)
    line = ''.join(l)
    if len(line) == width:
        increment = -2
        print(center.center(width, '-'))
    else:
        print(line.center(width, '-'))
    element_counter += increment