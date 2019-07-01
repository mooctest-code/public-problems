'''TESTCASE
3.0 4.0
6.0 0
-
1.4 -2.0
1.5 4.2
-
-1 1.2
-3.2 5
-
0 0
0 0
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, rhs):
        return ((self.x-rhs.x)**2+(self.y-rhs.y)**2)**0.5


x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

p1 = Point(x1, y1)
p2 = Point(x2, y2)

print('{:.2f}'.format(p2 - p1))
