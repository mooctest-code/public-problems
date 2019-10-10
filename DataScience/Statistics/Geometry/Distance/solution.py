'''TESTCASE
0 1 0 1
1 1 0 0
-
8.99 1.78 -7.53 -1.44 -1.79 -2.58
4.1 3.22 0.37 -5.0 3.49 0.76
-
1 2 3
4 5 6
-
6.08 -8.48 6.63 8.52 -0.53 -7.97 -1.0 6.72 -3.05 5.84
-4.28 -6.31 -6.78 2.28 -0.71 -2.2 -2.23 5.26 3.3 9.25
-
9.12 3.92 2.73 4.02 3.74 3.76 0.09 3.37 8.2 8.72
0.19 1.32 5.57 0.78 5.22 2.41 8.74 9.41 4.95 6.85
'''


def pnorm(X, p):
    if p == 'inf':
        return max(map(abs, X))
    return sum(map(lambda x: abs(x)**p, X)) ** (1/p)


def minkowskiDistance(x, y, p):
    return pnorm([z[0]-z[1] for z in zip(x, y)], p)


def myprint(*args):
    print(*map('{:.4f}'.format, args))


x = tuple(map(float, input().split()))
y = tuple(map(float, input().split()))

myprint(minkowskiDistance(x, y, 1),
        minkowskiDistance(x, y, 2),
        minkowskiDistance(x, y, 'inf'))
