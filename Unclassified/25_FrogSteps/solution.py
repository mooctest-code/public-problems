n = int(input())

f1, f2 = 1, 2

if n == 0: 
    f1 = 0

while n > 1:
    n -= 1
    f1, f2 = f2, f1+f2

print(f1)