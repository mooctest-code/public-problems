'''TESTCASE
Hello World!
-
This is a test text
-
Hola World!
-
fneakjnfoaidjkasopdhwquonr3o.e13[p.e13o2jme.12';e.;'1,e;'12.,dso21pmd12,'1e2,ep,[]]
'''
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