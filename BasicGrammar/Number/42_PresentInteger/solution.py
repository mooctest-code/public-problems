'''TESTCASE
413
-
34145
-
79675
-
-3467546
-
315318746
-
-123
'''
# http://www.pythontip.com/coding/report_detail/748/
n = int(input())
x=['0x'+('%02x'%((n&(0xff<<(x*8)))>>(x*8))).upper() for x in range(4)]
print(' '.join(x))