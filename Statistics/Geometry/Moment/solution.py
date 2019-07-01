'''TESTCASE
7.6 2.6 3.2 4.4 5.4 6.8 8.8
-
6.69 5.09 7.46 4.67 6.77 5.09
-
4.53 2.68 6.55 6.12 8.31 7.12 8.00 9.61 7.66 5.47 7.85 7.43 7.64 5.89 7.06 1.22 9.71 6.86 6.19 6.86
-
11.34 6.46 1.50 3.53 6.52 6.69 5.09 7.46 4.67 6.77 5.10 6.68 6.24 2.23 5.38 9.55
-
3 2 2 2 1 1 1 0
'''


def A(k: int, x):
    return sum(map(lambda xi: xi**k, x)) / len(x)


def B(k: int, x):
    if k == 1:
        return 0
    A1 = A(1, x)
    return sum(map(lambda xi: (xi-A1)**k, x)) / len(x)


x = list(map(float, input().split()))
for k in range(1, 5):
    print('{:.4f} {:.4f}'.format(A(k, x), B(k, x)))
