'''TESTCASE
0.15 0.1
-
0.2 0.2
-
0.2 0.15
-
0.1 0.3
'''

from scipy import stats

p1, p2 = map(float, input().split())

no = stats.norm(0, 1)

p = no.ppf(p1)
i = no.isf(p2)

u = p*50/(p-i) + 500
s = (500 - u) / p

print('{:.4f} {:.4f}'.format(u, s))
