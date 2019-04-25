n = int(input())

# prime list
prime = []
check = [False for i in range(n)]

for i in range(2, n):
    if not check[i]:
        prime.append(i)
    for j in range(0, len(prime)):
        if i * prime[j] >= n:
            break
        check[i*prime[j]] = True
        if i % prime[j] == 0:
            break
            
primeSet = set(prime)
cnt = 0
for i in range(0, len(prime)):
    if prime[i] < n-prime[i] and (n - prime[i]) in primeSet:
        cnt += 1

print(cnt)