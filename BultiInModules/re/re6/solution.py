import re
num = int(input())
for i in range(num):
    str1 = input()
    ret=re.findall('[1-9][0-9]{4,}',str1)
    print(ret)