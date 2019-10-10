'''TESTCASE
iris
-
digits
-
wine
-
breast_cancer
'''

from sklearn import datasets
import pandas as pd
from math import log


def getp(x: pd.Series):
    px = {}
    for idx, cnt in x.value_counts().items():
        px[idx] = cnt / x.size
    return px


def rel(p: dict, q: dict):
    return sum((p[i] * log(p[i]/q[i]) for i in p))


name = input()

dataset = eval('datasets.load_' + name + '()')

target = pd.Series(dataset['target'])

q = getp(target)

for i in (0.01, 0.1, 0.5, 0.9):
    p = getp(target.sample(frac=i, random_state=0))
    print('{:.6f}'.format(rel(p, q)))
