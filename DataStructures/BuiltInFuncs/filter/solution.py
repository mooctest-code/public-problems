#filter
import math

def is_sqr(x):
    return int(math.sqrt(x)) ** 2 == x

n, m = map(int, input().split())
print(*filter(is_sqr, range(n,m+1)))