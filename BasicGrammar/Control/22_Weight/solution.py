a = int(input())

n = 0
cnt = 0
while n < a:
    n = n + pow(3, cnt)
    cnt = cnt + 1

print(cnt)
