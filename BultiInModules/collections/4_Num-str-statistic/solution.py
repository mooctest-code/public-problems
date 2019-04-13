from collections import Counter

a = input()
cnt = Counter(a)
ans = [cnt[str(i)] for i in range(10)]

print(*ans)