a = int(input())

m = int(a ** 0.5)

cnt = 0
for i in range(1, m):
    if a % i == 0:
        cnt += 2

if m * m == a:
    cnt += 1

print(cnt)