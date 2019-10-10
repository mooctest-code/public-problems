'''TESTCASE
0 1
-
0 0.4
-
1 2
-
0 0.2
-
0.2 1.4
'''

from scipy import integrate

a, b = map(eval, input().split())

A = (a + b) * (b - a) / 2

r = 0
if a < 1:
    r, e = integrate.dblquad(lambda x, y: 1/A, a, min(b, 1),
                             lambda x: x**2, lambda x: x)
print('{:.4f}'.format(r))

r = 0
if a < 0.3:
    r, e = integrate.dblquad(lambda x, y: 1/A, a, min(b, 0.3),
                             0, lambda x: x)

print('{:.4f}'.format(r))
