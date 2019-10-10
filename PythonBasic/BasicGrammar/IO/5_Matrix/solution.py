'''TESTCASE
3 3
1 2 3
4 5 6
7 8 9
-1 0 1
1 2 3 4 5
13 14 15
12345
-
4 4
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
123 67 456 89 67 4432
872 463 32
432
12376432 123 1671
12367 3267
'''
n, m = map(int, input().split())
for i in range(n):
    a = map(int, input().split())
    print(*map(lambda x: x*2, a))

try:
    while True:
        print(sum(map(int, input().split())))
except EOFError:
    pass