'''TESTCASE
4 5 3
-
3 4 7
-
2 5 3
-
10 12 14
'''
s = list(map(int, input().split()))
s.sort()
[a, b, c] = s

area = 0

if a + b > c:
    l = (a + b + c) / 2
    area = (l*(l-a)*(l-b)*(l-c))**0.5

if not area:
    print('Can\'t construct a triangle.')
else:
    print('{} {:.2f}'.format(sum(s), area))
