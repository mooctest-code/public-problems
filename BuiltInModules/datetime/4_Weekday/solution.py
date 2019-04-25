from datetime import date

y, m, d = map(int, input().split('-'))
dt = date(y, m, d)
print(dt.strftime("%A"))