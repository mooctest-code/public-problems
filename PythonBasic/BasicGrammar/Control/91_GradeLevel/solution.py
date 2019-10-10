'''TESTCASE
[100, 54, 34, 84]
-
[42, 65, 61, 99]
-
[100, 90, 70, 74]
'''
print([chr(ord('A')+((abs(100-i-1)//10) if i > 59 else 5)) for i in eval(input())])