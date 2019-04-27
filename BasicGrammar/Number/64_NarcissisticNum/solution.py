'''TESTCASE
None
'''
l = []
for i in range(100, 1000):
    if (i//100) ** 3 + ((i//10)%10) ** 3 + (i % 10) ** 3 == i:
        l.append(i)

print(' '.join(map(str, l)))