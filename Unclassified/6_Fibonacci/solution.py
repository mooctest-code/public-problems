n = int(input())

f0, f1 = 0, 1
for i in range(n-1):
    f0, f1 = f1, f0+f1

print(f0) 