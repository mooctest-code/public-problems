'''TESTCASE
0 1 0 1
1 1 0 1
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

import numpy as np


def cosine(x, y):
    v1 = np.array(x)
    v2 = np.array(y)
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    return v1 @ v2 / (n1 * n2)


x = tuple(map(float, input().split()))
y = tuple(map(float, input().split()))

print('{:.4f}'.format(cosine(x, y)))
