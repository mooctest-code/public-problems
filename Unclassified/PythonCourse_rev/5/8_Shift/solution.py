'''TESTCASE
37
-
12
-
9
-
19
-
75
'''
i = int(input())
true = True
for j in range(2, 100):
    k = i * j
    if k < 99:
        continue
    if k > 999:
        break
    s = str(k)
    if int(s[1:]+s[0]) % i or int(s[-1]+s[:-1]) % i:
        true = False
        break

print('这是一个{}命题'.format('真' if true else '假'))
