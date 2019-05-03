'''TESTCASE
2019-08-29
-
1900-10-01
-
2000-10-01
-
2000-01-01
'''
from datetime import date

y, m, d = map(int, input().split('-'))
d1 = date(y, m, d)
d2 = date(y, 1, 1)

print((d1 - d2).days + 1)