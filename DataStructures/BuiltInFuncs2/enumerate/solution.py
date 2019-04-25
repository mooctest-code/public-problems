#enumerate
num = int(input())
for i in range(num):
    listEmp = list(input().split())
    for i,element in enumerate(listEmp,start = 10001):
        print(i,element)