#filter
import math
num = int(input())
def is_sqr(x):
    return math.sqrt(x) % 1 == 0

for i in range(num):
    res = []
    str1 = list(map(int,input().split()))
    n = str1[0]
    m = str1[1]
    newlist = filter(is_sqr, range(n,m+1))
    for j in newlist:
        res.append(j)
    print(res)