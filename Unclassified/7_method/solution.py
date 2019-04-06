l = eval(input())

n = []

for i in l:
    if i[1] >= 80:
        n.append(i[0])

print(n)