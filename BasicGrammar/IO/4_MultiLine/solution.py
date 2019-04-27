'''TESTCASE
1
2
3
-
-1
0
1
'''
try:
    while True:
        a = int(input())
        print(a)
except EOFError:
    pass
