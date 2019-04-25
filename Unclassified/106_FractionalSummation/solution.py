a = int(input())

ans = 0
u = 2
d = 1
for i in range(0, a):
    ans += u / d
    d, u = u, d + u

print('%.2f' % ans)