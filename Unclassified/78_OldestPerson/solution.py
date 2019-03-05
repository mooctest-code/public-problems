d = eval(input())

maxkv = ('', 0)
for k, v in d.items():
    if v > maxkv[1]:
        maxkv = (k, v)

print(maxkv[0])