'''TESTCASE
42
-
240
-
210
-
32488
-
604800
'''
# http://www.pythontip.com/coding/report_detail/1720/

k = int(input())

n=k
m=k-1
r=k//2+1
while r>1:
    tmpk=k
    tmpr=r
    while tmpk>1 and tmpk%tmpr==0 and tmpr>1:
        tmpk=tmpk//tmpr
        tmpr-=1
    if tmpk==1:
       n=r
       m=tmpr        
    r=r-1

print((n, m))