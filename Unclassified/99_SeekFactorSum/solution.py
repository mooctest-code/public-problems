n = int(input())

k = 1
ans = 0
for i in range(1, n+1):
    k *= i
    ans += k

print(ans)