dic = {}
while True:
    try:
        s = input().split(' ')
        dic[s[0]] = s[1]
    except:
        break
print(repr(dic))
