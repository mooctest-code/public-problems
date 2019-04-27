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
t = datetime.fromtimestamp(float(input()))
print(t.strftime("%Y-%m-%d %H:%M"))