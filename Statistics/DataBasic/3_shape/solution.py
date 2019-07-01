'''TESTCASE
0
-
10
-
20
-
14
'''
import numpy as np

np.random.seed(int(input()))

a = np.random.randint(0, 20, (3, 4))
print('a:\n', a)

ha1, ha2 = np.hsplit(a, 2)
print('ha1:\n', ha1)

va1, va2, va3 = np.vsplit(a, 3)
print('va1:\n', va1)

print('hstack:\n', np.hstack((ha1, ha2)))
print('vstack:\n', np.vstack((va1, va2)))

print('a:\n', a.flatten())
