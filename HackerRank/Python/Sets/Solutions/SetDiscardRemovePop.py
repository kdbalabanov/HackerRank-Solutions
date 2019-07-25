n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    user_in = input().split()
    op = user_in[0]
    if len(user_in) > 1:
        exec('s.' + op + '(' + user_in[1] + ')')
    else:
        exec('s.' + op + '()')
print(sum(s))