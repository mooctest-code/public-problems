from collections import Counter
from functools import cmp_to_key

def cmp(a, b):
    if a[1] == b[1]:
        if a[0] < b[0]:
            return -1
        else: return a[0] > b[0]
    else: return -1 if a[1] > b[1] else 1

num = int(input())
fruitList = Counter(input().split()).most_common()

fruitList.sort(key=cmp_to_key(cmp))

for fruit in fruitList:
    print('{} {}'.format(*fruit))