from itertools import permutations

a = map(int, input().split(' '))
for i in permutations(a, 3):
    print('{}{}{}'.format(i[0], i[1], i[2]))
