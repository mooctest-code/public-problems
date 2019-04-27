'''TESTCASE
2019-02-01 23:21
2019-01-03 12:35
-
2019-02-01 23:21
2017-01-03 12:35
-
2014-03-01 21:21
2017-01-03 12:35
-
2017-01-01 23:21
2017-01-01 12:00
'''
from datetime import datetime


def get_dt():
    return datetime.strptime(input(), "%Y-%m-%d %H:%M")

d1 = get_dt()
d2 = get_dt()

delta = abs(d1 - d2)
print(delta.days, delta.days*24+delta.seconds//3600)