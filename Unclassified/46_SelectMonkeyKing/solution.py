n, m = map(int, input().split())

r = 0
for i in range(2, n+1):
    r = (r + m) % i

print(r + 1)