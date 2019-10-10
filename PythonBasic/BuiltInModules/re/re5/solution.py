'''TESTCASE
1
iselab 123 mooc 456 huidhui
1 20
-
2
iselab 123 mooc 456 huidhui
1 7
iselab 123 mooc 456 huidhui
1 17
'''

import re 
num = int(input())
for i in range(num):
    str1 = input()
    str2 = list(map(int,input().split()))
    startPoint = str2[0]
    endPoint = str2[1]
    pattern = re.compile(r'\d+')   # 查找数字
    print(pattern.findall(str1,startPoint,endPoint)) 