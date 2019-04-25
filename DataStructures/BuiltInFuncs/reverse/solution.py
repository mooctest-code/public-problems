#reverse
s = list(map(int, input().split()))

print(*reversed(s))
print(*s[::-1])
s.reverse()
print(*s)