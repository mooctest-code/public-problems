'''TESTCASE
A candle lights others and consumes itself.
an
-
Woyebuzhidaoyinggaixiexieshenmedongxi
ng
-
zhegeceshiyonglihaonanxiea,shizaibuhuixieceshiyongli
hi
-
NNN
NN
'''
s1 = input()
s2 = input()

l2 = len(s2)
cnt = 0
for i in range(len(s1)):
    if s1[i:len(s2)+i] == s2:
        cnt += 1

print(cnt)