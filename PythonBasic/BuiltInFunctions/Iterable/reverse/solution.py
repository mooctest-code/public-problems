'''TESTCASE
1 2 3
-
1 2 3 4 5
'''
#reverse
s = list(map(int, input().split()))

print(*reversed(s))
print(*s[::-1])
s.reverse()
print(*s)