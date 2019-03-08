n = int(input())
s = 0
for i in range(n):
    a = list(map(int, input().split()))
    s += a[i]
print(s)