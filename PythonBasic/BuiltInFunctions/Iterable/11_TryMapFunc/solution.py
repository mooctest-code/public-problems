'''TESTCASE
1 2 3 4 5
-
-1 -2 -3
'''
print(' '.join(map(lambda x: str(x+10), map(int, input().split()))))