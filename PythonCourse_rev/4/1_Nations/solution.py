'''TESTCASE
3
China Chinese
USA English
France French
-
4
China Chinese
England English
Germany German
Spain Spanish
'''
n = int(input())

nations = {}
for i in range(n):
    c, l = input().split()
    nations[c] = l

print(*sorted(nations.keys()))
print(*sorted(nations.values()))
print(*['{}-{}'.format(c, l) for (c, l) in sorted(nations.items())])
print(nations.get('France', 'Unknown'))

nations.update({'Spain': 'Spanish', 'Japan': 'Japanese'})
print(*sorted(nations.keys()))
