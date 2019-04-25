from datetime import date

y, m, d = map(int, input().split('-'))
d1 = date(y, m, d)
d2 = date(y, 1, 1)

print((d1 - d2).days + 1)