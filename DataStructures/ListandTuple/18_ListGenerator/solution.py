'''TESTCASE
3 7
-
10 20
'''
[a, b] = list(map(int, input().split()))
print([i**2 for i in range(a, b+1)])