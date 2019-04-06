import operator

a = eval(input())

m = {}
for key in a:
    m[a[key]] = key

print(dict(sorted(m.items(), key=operator.itemgetter(0))))