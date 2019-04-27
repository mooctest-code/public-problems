'''TESTCASE
1
3344,88888,7778957,10000,99999,414,4,867287672
-
1
HUADIH,hudi890283,7808908
-
1
DHAUDAD,78193,327389,3893D,8929
-
2
337554874,14542784,1254,3654789,14,2
shudau,sdhidhai,dsooadb,zcjiso,12547896
'''
import re
num = int(input())
for i in range(num):
    str1 = input()
    ret=re.findall('[1-9][0-9]{4,}',str1)
    print(ret)