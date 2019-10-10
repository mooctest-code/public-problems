'''TESTCASE
alcohol
-
malic_acid
-
ash
-
alcalinity_of_ash
-
proline
'''

from sklearn import datasets
import numpy as np
from math import log


def h(cnt, total: int):
    if total == 0:
        return 0

    ent = 0
    for i in cnt:
        p = i / total
        if p > 0:
            ent -= p * log(p)
    return ent


def cond(data: list, target: list, target_names: list):
    size = len(data)
    assert(size > 0)

    len_target = len(target_names)

    tc = np.array([0 for i in range(len_target)])
    ttc = np.array([target.count(i) for i in range(len_target)])

    data = sorted(zip(data, target))

    min_ent = h(ttc, size)

    def_ent = min_ent

    i = 0
    while i < size:
        tc[data[i][1]] += 1
        while i < size-1 and data[i+1][0] == data[i][0]:
            tc[data[i+1][1]] += 1
            i += 1

        l = i + 1
        r = size - l

        left_ent = h(tc, l)
        right_ent = h(ttc-tc, r)
        ent = l/size * left_ent + r/size * right_ent

        if ent <= min_ent:
            if ent < min_ent:
                min_ent = ent
                ans = []
            ans.append(data[i][0])

        i += 1

    return def_ent, min_ent, ans


dataset = datasets.load_wine()

name = input()

idx = dataset['feature_names'].index(name)

data = [d[idx] for d in dataset['data']]

d, m, ans = cond(data,
                 dataset['target'].tolist(),
                 dataset['target_names'])

print('{:.6f} {:.6f}'.format(d, m))
print(*ans)
