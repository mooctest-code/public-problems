'''TESTCASE
10 4
-
5 0
-
41231 123
-
3242 32
-
321 34
-
42358294 12322
-
34324353 16257
'''
n, k = map(int, input().split())

print(n&k == k)