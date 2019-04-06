l = []
for i in range(3):
    [n, p, r] = [eval(input()) for j in range(3)]
    if p == '110M':
        l.append((n, r))

print(l)