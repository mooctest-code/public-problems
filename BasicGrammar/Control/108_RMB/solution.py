a = [1, 2, 5]
n = 100

cnt = 0
for i in range(0, (n//5)+1):
    for j in range(0, (n//2)+1):
        x = i * 5 + j * 2
        if x > n: break
        for k in range(0, n+1):
            y = x + k
            if y > n:
                break
            elif y == n:
                cnt += 1

print(cnt)