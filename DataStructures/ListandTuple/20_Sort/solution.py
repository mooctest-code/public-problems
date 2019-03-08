n = int(input())
l = list(map(int, input().split()))
l.sort()
print(' '.join(map(str, l)))