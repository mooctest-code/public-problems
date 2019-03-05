n = int(input())
a = map(int, input().split())
s = set(a)
z = 0 in s
l = len(s)
print((l-z)*(l-1))
