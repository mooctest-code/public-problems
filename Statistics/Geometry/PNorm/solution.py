'''TESTCASE
4.59 4.06 1.4 2.26 4.7 5.35 6.28 2.23
2
-
-5.08 -8.85 5.09 -8.44 7.34 5.94 -3.68 2.64
1
-
-9.71 8.69 0.45 -3.19
inf
-
-5.08 -8.85 5.09 -8.44 7.34 5.94 -3.68 2.64
2
-
4.59 4.06 1.4 2.26 4.7 5.35 6.28 2.23
4
'''


def pnorm(X, p):
    if p == 'inf':
        return max(map(abs, X))
    return sum(map(lambda x: abs(x)**p, X)) ** (1/p)


X = list(map(float, input().split()))

p = input()
p = int(p) if p != 'inf' else p

print('{:.4f}'.format(pnorm(X, p)))
