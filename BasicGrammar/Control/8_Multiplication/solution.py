n = int(input())

for i in range(1, n+1):
    print(' '.join('%d*%d=%d' % (i, j, i*j) for j in range(1, i+1)))