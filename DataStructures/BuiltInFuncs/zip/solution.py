#zip
str1 = list(input().split(','))
str2 = list(input().split(','))
zipped = zip(str1,str2)
for i in zipped:
    print(i)