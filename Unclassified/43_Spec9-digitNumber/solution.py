'''TESTCASE
2
-
4
-
7
-
9
'''
# http://www.pythontip.com/coding/report_detail/1651/

isfind=0
def make(i,s):
    global isfind,n
    if isfind:
        return
    else:
        if i==n and isfind==0:
            print(int(s))
            isfind=1
        else:
            for k in range(1,10):
                s2=s+str(k)
                if str(k) not in s and int(s2)%(i+1)==0:
                    make(i+1,s2)

n = int(input())               
make(0, '')