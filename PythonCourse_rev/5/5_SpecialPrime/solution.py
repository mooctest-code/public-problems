'''TESTCASE
290
-
100
-
999
-
600
'''


def is_prime(a):
    if a < 2:
        return False
    if a % 2 == 0:
        return a == 2
    x = int(a ** 0.5)+1
    for i in range(3, x, 2):
        if a % i == 0:
            return False
    return True


def find(iterable, default):
    for i in iterable:
        s = list(map(int, str(i)))
        if (s[2] + s[1]) % 10 == s[0] and is_prime(i):
            return i
    return default


x = int(input())

l = find(range(100, x), -2000)
r = find(range(x+1, 1000), 2000)

dl, dr = x - l, r - x

print(l if dl < dr else r)
