n, m = map(int, input().split())
for i in range(n):
    a = map(int, input().split())
    print(*map(lambda x: x*2, a))

try:
    while True:
        print(sum(map(int, input().split())))
except EOFError:
    pass