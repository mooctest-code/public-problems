'''TESTCASE
0.01 0.2 0.03
-
0.03 0.2 0.01
-
0.4 0.05 0.2
-
0.02 0.2 0.02
'''

a, b, c = map(float, input().split())

pj0 = a + c
pi1 = a / pj0
pi2 = c / pj0
pj1 = b / pi1
pj2 = 1 - pj0 - pj1

print('P(i,j)\tj=0\tj=1\tj=2\tP(i)')
print('i=1\t{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}'.format(a, b, pi1*pj2, pi1))
print('i=2\t{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}'.format(c, pi2*pj1, pi2*pj2, pi2))
print('P(j)\t{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}'.format(pj0, pj1, pj2, 1))
