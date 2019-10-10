'''TESTCASE
1996
-
2000
-
2100
-
3478
-
2019
-
2003
'''
a = int(input())
print(a % 400 == 0 or (a % 4 == 0 and a % 100 != 0))