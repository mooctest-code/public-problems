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
dt = date(y, m, d)
print(dt.strftime("%A"))