'''TESTCASE
1 2 3 4
-
9 8 7 6
-
2 3 6 7
-
2 4 6 8
'''
from itertools import permutations

a = sorted(input().split())
cnt = 0
for i in permutations(a, 3):
    (cnt, end) = (0, '\n') if cnt == 3 else (cnt+1, ' ')
    print(''.join(i), end=end)
