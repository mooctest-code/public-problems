import random
from collections import Counter

random.seed(0)

n = int(input())

l = [random.randint(0, 9) for i in range(n)]

c = Counter(l).most_common()

c.sort()

for i in c:
    print('{} {}'.format(i[0], i[1]))