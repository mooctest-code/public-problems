import re
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
num = int(input())
for i in range(num):
    str1 = input()
    print(re.sub('(?P<value>\d+)', double, str1))