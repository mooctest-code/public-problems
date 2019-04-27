'''TESTCASE
2
ise www.iselab.cn
com www.iselab.cn
-
1
www www.baidu.com
-
2
www www.baidu.com
buzhidao woyebuzhidao
-
1
emmmmmmm emmmmnmmmm
'''

import re
num = int(input())
for i in range(num):
    str1 = list(input().split())
    pattern = str1[0]
    strToSearch = str1[1]
    if(re.search(pattern,strToSearch)):
        print(re.search(pattern,strToSearch).span())
    else:
        print(re.search(pattern,strToSearch))