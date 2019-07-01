'''TESTCASE
7.6 2.6 3.2 4.4 5.4 6.8 8.8
-
6.69 5.09 7.46 4.67 6.77 5.09
-
4.53 2.68 6.55 6.12 8.31 7.12 8.00 9.61 7.66 5.47 7.85 7.43 7.64 5.89 7.06 1.22 9.71 6.86 6.19 6.86
-
11.34 6.46 1.50 3.53 6.52 6.69 5.09 7.46 4.67 6.77 5.10 6.68 6.24 2.23 5.38 9.55
-
11.34 3.53 6.52 6.46 8.31 7.12 1.50 6.69 5.09 7.46 4.67 6.77
'''

import numpy as np
from math import floor, ceil
from scipy import stats


def myprint(*args):
    args = ['{:.2f}'.format(i) for i in args]
    print(*args)


def ishalf(x: float):
    return x - floor(x) == 0.5


a = np.array(list(map(float, input().split())))
a.sort()
l = a.size
myprint(*(np.quantile(a, i, interpolation='midpoint' if ishalf((l-1)*i) else 'nearest')
          for i in (0.25, 0.5, 0.75)))

Q = []
for i in (0.25, 0.5, 0.75):
    q = (l+1) * i - 1
    if ishalf(q):
        Q.append((a[floor(q)]+a[ceil(q)])/2)
    else:
        Q.append(a[round(q)])

myprint(*Q)
