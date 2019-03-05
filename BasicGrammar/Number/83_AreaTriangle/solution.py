s= list(map(int, input().split()))
s.sort()
[a, b, c] = s

area = 0

if a + b > c:
    l = (a + b + c) / 2
    area = (l*(l-a)*(l-b)*(l-c))**0.5

if not area:
    print(0)
else: print('{:.3f}'.format(area))

