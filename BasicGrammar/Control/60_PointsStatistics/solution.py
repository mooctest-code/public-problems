s = input()

t = 0
k = 1
for i in s:
    if i == 'A':
        t += k
        k += 1
    else: k = 1

print(t)