#map
num = int(input())
for i in range(num):
    str1 = list(map(int,input().split()))
    print(sum(str1))
    print(max(str1))