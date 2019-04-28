'''TESTCASE
en¿
-
这是一个中文例子
-
😋
-
↑　↓　→　←
'''
a = input()
ans = []
for i in a:
    asc = ascii(i).strip('\'')
    if asc != i:
        ans.append(asc)
print(*ans)