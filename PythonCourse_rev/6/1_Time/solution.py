'''TESTCASE
1555134795.4250443
-
4738295.54372
-
123789763.43671
-
3104.123788
'''
from datetime import datetime
from datetime import date
t = datetime.fromtimestamp(float(input()))
print(t.strftime("%Y-%m-%d %H:%M"))

d1 = t.date()
d2 = date(t.year, 1, 1)

print('是{}年的第{}天'.format(t.year, (d1 - d2).days + 1))
