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

from math import log


def entropy(x: list):
    l = len(x)
    ent = 0
    for i in set(x):
        p = x.count(i) / l
        ent -= p * log(p)
    return ent


name = input()

target = eval('datasets.load_' + name + '()')['target']

print('{:.4f}'.format(entropy(target.tolist())))
