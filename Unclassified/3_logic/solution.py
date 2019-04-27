'''TESTCASE
'32'
'1'
'1'
'32'
-
'Hello'
' World'
'Hell'
'o World'
-
1
3
2
2
'''
[a, b, c, d] = [eval(input()) for i in range(4)]

print('\'{}\' == \'{}\' is {}'.format(a+b, c+d, a+b == c+d))