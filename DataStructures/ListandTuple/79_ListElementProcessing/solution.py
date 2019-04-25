l = eval(input())
t = eval(input())
n = int(input())

l[t[0]] = t[1]

print(list(filter(lambda x: x != n, l)))