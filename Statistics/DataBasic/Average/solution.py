'''TESTCASE
7.6 2.6 3.2 4.4 5.4 6.8 8.8
-
1.08 1.09 1.10 1.12 1.12
-
4.53 2.68 6.55 6.12 8.31 7.12 8.00 9.61 7.66 5.47 7.85 7.43 7.64 5.89 7.06 1.22 9.71 6.86 6.19 6.86
-
11.34 6.46 1.50 3.53 6.52 6.69 5.09 7.46 4.67 6.77 5.10 6.68 6.24 2.23 5.38 9.55
-
11.34 3.53 6.52 6.46 8.31 7.12 1.50 6.69 5.09 7.46 4.67 6.77
'''

from functools import reduce


def myprint(*args):
    args = ['{:.4f}'.format(i) for i in args]
    print(*args)


a = list(map(float, input().split()))
l = len(a)
A = sum(a) / l
G = reduce(float.__mul__, a) ** (1/l)
H = l / sum(map(lambda x: 1/x, a))
Q = (sum(map(lambda x: x*x, a)) / l) ** 0.5

myprint(A, G, H, Q)
