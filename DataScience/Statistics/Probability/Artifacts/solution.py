'''TESTCASE
3
0.02 0.01 0.03
0.15 0.80 0.05
-
4
0.01 0.02 0.03 0.04
0.4 0.3 0.2 0.1
-
2
0.03 0.02
0.4 0.6
-
1
0.02
1.0
'''


def fprint(*args):
    print(*map(lambda x: '{:.4f}'.format(x), args))


n = int(input())
p = list(zip(map(float, input().split()),
             map(float, input().split())))
pa = 0
for pab, pb in p:
    pa += pab * pb

fprint(pa)

pba = []
for pab, pb in p:
    pba.append(pab*pb/pa)

fprint(*pba)
