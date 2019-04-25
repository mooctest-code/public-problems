a = int(input())

ans = []
while a != 1:
    if a % 2 == 0:
        x = a // 2
        ans.append('{}/2={}'.format(a, x))
        a = x
    else:
        x = a * 3 + 1
        ans.append('{}*3+1={}'.format(a, x))
        a = x

for i in ans:
    print(i)