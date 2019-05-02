'''TESTCASE
{'Wangbing': 1001, 'Maling': 1003, 'Xulei': 1005}
-
{'Wangbing': 1001, 'Xulei': 1005, 'Maling': 1003}
'''
import operator

a = eval(input())

m = {}
for key in a:
    m[a[key]] = key

print(dict(sorted(m.items(), key=operator.itemgetter(0))))