#reverse
num = int(input())
for i in range(num):
    str1 = list(input().split())
    num = int(str1[1])
    strLeft = list(str1[0][:num])
    strRight =list(str1[0][num:])
    strLeft.reverse()
    strRight.reverse()
    strLeft.extend(strRight)
    strLeft.reverse()
    print(''.join(strLeft))