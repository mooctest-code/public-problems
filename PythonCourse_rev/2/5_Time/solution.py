'''TESTCASE
10000000
-
1
-
12345
-
12345678
'''
a = int(input())

dd = 24 * 60
dy = 365 * dd

y = a // dy
a %= dy
d = a // dd
h = a % dd // 60
m = a % dd % 60

print('{}年零{}天零{}小时零{}分钟'.format(y, d, h, m))
