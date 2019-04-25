import re
num = int(input())
for i in range(num):
    str1 = input()

    number = re.sub(r'\D',"",str1)
    print(number)