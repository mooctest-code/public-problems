[a, b] = list(map(int, input().split()))

for i in range(1, b+1):
    if b % i == 0:
        j = b // i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            print(((i-j)//2)**2 - a)

