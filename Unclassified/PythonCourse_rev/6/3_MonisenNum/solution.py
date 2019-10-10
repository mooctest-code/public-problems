'''TESTCASE
2
-
3
-
4
-
5
-
6
'''


def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2

    k = int(n ** 0.5)+1
    for i in range(3, k, 2):
        if n % i == 0:
            return False
    return True


def getMonisen(n):
    cnt = 0
    p = 3
    while True:
        m = 2 ** p - 1
        if isPrime(p) and isPrime(m):
            cnt += 1
            if cnt == n:
                return m
        p += 2


n = int(input())
print(getMonisen(n))
