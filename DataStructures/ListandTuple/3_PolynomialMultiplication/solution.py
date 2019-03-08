import numpy as np

f = np.poly1d(np.array(eval(input())))
g = np.poly1d(np.array(eval(input())))

product = (f*g).coef.tolist()
print([round(x, 3) for x in product])