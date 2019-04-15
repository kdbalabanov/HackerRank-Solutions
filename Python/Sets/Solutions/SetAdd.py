# Enter your code here. Read input from STDIN. Print output to STDOUT
result = set()
num = int(input())
for i in range(num):
    result.add(str(input()))
print(len(result))