'''TESTCASE
2 37 100
-
10 37 60
-
5 20 90
-
1 100 100
'''
m, t1, t2 = map(int, input().split())

print('{}J'.format(m*(t2-t1)*4184))
