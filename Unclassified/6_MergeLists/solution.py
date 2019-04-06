n = int(input())
a = input().split()
b = [int(i) for i in input().split()]

for i in range(n):
    print('{}: {}'.format(a[i], b[i]))