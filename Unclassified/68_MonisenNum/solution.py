def isPrime(n):
    if n == 2: 
        return True
    k = int(n ** 0.5)
    for i in range(3, k, 2):
        if n % i == 0:
            return False
    return True

def getMonisen(n):
    l = [3]
    p = 3
    while True:
        m = 2 ** p - 1
        if isPrime(p) and isPrime(m):
            l.append(m)
            if len(l) == n:
                return l
        p += 2

n = int(input())
l = getMonisen(n)
for i in l:
    print(i, end=' ' if i != l[-1] else '\n')