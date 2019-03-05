def phi(n):
    p, i = n, 2
    while i * i < n:
        if n % i == 0:
            p = p // i * (i-1)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1: p = p // n * (n-1)
    return p

n = int(input())
print(phi(n))