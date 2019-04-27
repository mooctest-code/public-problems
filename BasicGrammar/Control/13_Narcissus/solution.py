'''TESTCASE
123
-
370
-
372
-
400
-
999
'''
nar = [153, 370, 371, 407]
a = int(input())
dif = 999
ans = 0
for i in nar:
    d = abs(a-i)
    if d < dif:
        dif = d
        ans = i
print(ans)