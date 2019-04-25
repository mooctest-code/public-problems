[a, b, c] = map(int, input().split())

if c < b:
    c, b = b, c
if b < a:
    b, a = a, b
if c < b:
    c, b = b, c

print('{} {} {}'.format(a, b, c))
