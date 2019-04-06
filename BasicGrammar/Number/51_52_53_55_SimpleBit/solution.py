a, b = map(int, input().split())

print(a&b)
print(a|b)
print(a^b)
a = ~a
b = ~b
print(b if a > b else a)