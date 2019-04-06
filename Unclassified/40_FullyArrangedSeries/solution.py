from itertools import permutations

n, k = map(int, input().split())

for i in permutations('123456789'[0:n], n):
    if k == 1: 
        print(''.join(i))
        break
    k -= 1
