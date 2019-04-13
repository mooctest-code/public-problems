from collections import Counter
import functools

def cmp(x, y):
    if x[1] == y[1]:
        return -1 if x[0] < y[0] else x[0] > y[0]
    return -1 if x[1] > y[1] else x[1] < y[1]

l = Counter(filter(str.isalpha, input().lower())).most_common()
l.sort(key=functools.cmp_to_key(cmp))
for i in l:
    print('{} {}'.format(i[0], i[1]))