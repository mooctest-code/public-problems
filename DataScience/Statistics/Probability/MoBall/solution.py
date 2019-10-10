'''TESTCASE
4 2
-
0 1
-
1 0
-
0 0
-
10 0
-
10 10
'''
from functools import reduce


def fprint(x):
    print('{:.4f}'.format(x))


def f(a, b):
    return reduce(int.__mul__, (i for i in range(a, b+1)), 1)


def A(n, m):
    if n and m:
        return f(n-m+1, n)
    return 0


def C(n, m):
    if m == 0:
        return 0
    return A(n, m) // f(2, m)


n, m = map(int, input().split())

if n == 0:
    fprint(0)
    fprint(0)
elif m == 0:
    fprint(n > 0)
    fprint(n > 1)
else:
    fprint((n/(n+m))**2)
    fprint(C(n, 2)/C(n+m, 2))
