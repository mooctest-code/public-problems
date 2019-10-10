'''TESTCASE
6
-
8
-
1
-
4
'''

s = input()
i = int(s)
num = list(map(str, filter(lambda x: x % i and s not in str(x),
                           range(1, 101))))
for i in range(0, len(num), 10):
    print(','.join(num[i:i+10]))
