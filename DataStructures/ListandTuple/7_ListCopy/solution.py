'''TESTCASE
[1, 2, 3]
-
[7, 4, 3]
'''
l1 = eval(input())
l2 = l1.copy()
l2[0] = 0
print(l2)
print(l1)
