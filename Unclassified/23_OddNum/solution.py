a = int(input())

s = [0, 4, 28]

while a >= len(s):
    s.append(s[len(s)-1]*8)

print(sum(s[0:a+1]))
