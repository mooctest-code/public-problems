'''TESTCASE
10
-
999
-
1
-
12345
-
98765
'''

import random
from collections import Counter
random.seed(0)


def myprint(*args):
    args = ['{:.2f}'.format(i) for i in args]
    print(*args)


n = int(input())
r = (random.randint(0, 5) for i in range(n))
cnt = Counter(r)

myprint(*(cnt.get(i, 0)/n for i in range(6)))
