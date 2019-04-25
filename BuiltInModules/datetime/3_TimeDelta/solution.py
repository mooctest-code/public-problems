from datetime import datetime


def get_dt():
    return datetime.strptime(input(), "%Y-%m-%d %H:%M")

d1 = get_dt()
d2 = get_dt()

delta = abs(d1 - d2)
print(delta.days, delta.days*24+delta.seconds//3600)