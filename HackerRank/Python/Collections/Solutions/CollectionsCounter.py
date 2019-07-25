# Enter your code here. Read input from STDIN. Print output to STDOUT
X = int(input())
shoe_sizes = input().split()
n = int(input())
result = 0
for i in range(n):
    user_input = tuple(map(int, input().split()))
    shoe_size = str(user_input[0])
    if shoe_size in shoe_sizes:
        result += user_input[1]
        shoe_sizes.remove(shoe_size)
print(result)