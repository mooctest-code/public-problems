a = int(input())
print(a % 400 == 0 or (a % 4 == 0 and a % 100 != 0))