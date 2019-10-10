class Point:
    # TODO 实现 __init__ 存储坐标

    # TODO 实现 __sub__ 计算返回两个坐标的直线欧式距离
    pass


x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

p1 = Point(x1, y1)
p2 = Point(x2, y2)

print('{:.2f}'.format(p2 - p1))
