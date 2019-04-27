'''TESTCASE
6
-
20
-
123
-
654
'''
def sum(n): 
    return int(n*(n+1)*(2*n+1)/6)

N = int(input())

m = int(N**0.5) 
s = 0 
i = 1
while i <= N**(1/2.0): 
    s = s + i**2*(N//i) 
    if i**2 != N: 
        s = s + (sum(N//i) - sum(m)) 
    i = i + 1

print(s)