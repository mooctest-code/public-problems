'''TESTCASE
a b
-
b a
-
? ~
-
~ ?
'''
a, b = input().split()
print(abs(ord(a) - ord(b)))