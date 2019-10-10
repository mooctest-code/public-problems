'''TESTCASE
80 0.99
-
37 0.95
-
37 0.99
-
60 0.97
-
80 0.80
'''
from scipy import stats

c, p = map(float, input().split())

no = stats.norm(0, 1)

print('{:.2f}'.format(c - no.isf(p)*0.5))

# l, r = 0, 100
# s = 0.5
# while True:
#     m = (l + r) / 2
#     t = stats.norm.sf(c, m, s)
#     # print(t)
#     if t - p < -1e-4:
#         l = m
#     elif t - p > 1e-4:
#         r = m
#     else:
#         print('{:.2f}'.format(m))
#         break
