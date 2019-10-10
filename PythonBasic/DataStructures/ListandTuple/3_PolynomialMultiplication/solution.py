'''TESTCASE
[2, 0, -1.1, 1]
[1, 2.2, 1]
-
[1.0, -1.5, 2.0, 3.0]
[1.0, 0, 1.4]
-
[1.340, -4.2, 43.1, 2.23, 0.4]
[2.0, 0.432, 1.4, 0.4, -1.2]
'''
import numpy as np

f = np.poly1d(np.array(eval(input())))
g = np.poly1d(np.array(eval(input())))

product = (f*g).coef.tolist()
print([round(x, 3) for x in product])