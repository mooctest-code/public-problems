p = input()
l = eval(input())

print(['{} {}{}'.format(i, p, l[i]) for i in range(len(l))])