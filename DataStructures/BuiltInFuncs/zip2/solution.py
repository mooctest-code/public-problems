#zip2
str1 = list(input().split(','))
zipped = zip(str1[:-1],str1[1:])
for i in zipped:
    print(i)