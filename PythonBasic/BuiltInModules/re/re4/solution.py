'''TESTCASE
1
A23G4HFD567
-
1
a1234567dhiahdudha12
-
2
agdshadgjh
emmmm156795sdab4568
'''
import re
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
num = int(input())
for i in range(num):
    str1 = input()
    print(re.sub('(?P<value>\d+)', double, str1))