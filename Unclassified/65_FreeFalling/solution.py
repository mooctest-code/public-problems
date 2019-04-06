n, m = map(int, input().split())

d = n
while m > 1:
    d += n
    n /= 2
    m -= 1

print(d, n)