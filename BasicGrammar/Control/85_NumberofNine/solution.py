a = int(input())

n = 9
while n % a != 0:
    n = n * 10 + 9

print(len(str(n)))