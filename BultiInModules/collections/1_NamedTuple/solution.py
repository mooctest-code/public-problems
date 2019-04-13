from collections import namedtuple

Point = namedtuple('Point', 'x y')

print(Point._make(map(int, input().split())))