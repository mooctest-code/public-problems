'''TESTCASE
1
某人的电话号码是130-2944-9921
-
1
15478shduhsud9642sdo33 #iadhi
-
2
154789嗯嗯嗯嗯64233
好像是个电话号码
'''
import re
num = int(input())
for i in range(num):
    str1 = input()

    number = re.sub(r'\D',"",str1)
    print(number)