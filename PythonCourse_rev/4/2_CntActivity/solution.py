'''TESTCASE
xiaoma xiaowang xiaoma xiaoliu xiaoma xiaoliu
-
xiaoma xiaowang xiaoliu xiaoma xiaoma xiaowang
-
a b c c b a b c b
-
a d b d e c c f c b a b c b
'''
a = input().split()

d = {}
for i in a:
    d.setdefault(i, 0)
    d[i] += 1

cnt = sorted(d.items())
for s, c in cnt:
    print('{}: {}'.format(s, c))
