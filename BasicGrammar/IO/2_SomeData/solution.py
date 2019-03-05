print(*input().split()[::-1])
print(*map(lambda x: '{:.2f}'.format(float(x)), input().split()[::-1]))