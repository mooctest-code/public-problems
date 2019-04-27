'''TESTCASE
./public/distrub.txt
-
./public/biography.txt
'''
from collections import Counter

filePath = input()
dirpath = __file__.split('/')[0:-1]
dirpath.append(filePath)
with open('/'.join(dirpath), 'r') as f:
    print(Counter(filter(str.isalpha, f.read().upper())).most_common(1)[0][0])
    