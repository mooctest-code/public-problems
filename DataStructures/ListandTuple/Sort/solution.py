'''TESTCASE
1 2 3
-
-3 4 5 3 1 2 3 5
-
4 3 2
-
1 2 3 4 5
'''

ls = list(map(int, input().split()))
ls.sort(reverse=True)
print(*ls)