from datetime import datetime
t = datetime.fromtimestamp(float(input()))
print(t.strftime("%Y-%m-%d %H:%M"))