
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