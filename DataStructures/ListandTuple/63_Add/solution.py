n = int(input())
l = list(map(int, input().split()))

cnt = 0
for i in range(len(l)):
    for j in range(i):
        if l[i] + l[j] == 9:
            cnt += 1

print(cnt)