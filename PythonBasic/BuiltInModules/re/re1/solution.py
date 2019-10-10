'''TESTCASE
1
www www.iselab.cn
-
1
www www.baidu.com
-
2
buzhidao woyebuzhidao
emmmmmm emmmmmmmmmm
'''
import re
num = int(input())
for i in range(num):
    str1 = list(input().split())
    pattern = str1[0]
    strToMatch = str1[1]
    if(re.match(pattern,strToMatch)):
        print(re.match(pattern,strToMatch).span())
    else:
        print(re.match(pattern,strToMatch))