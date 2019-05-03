'''TESTCASE
3
-
34
-
78
-
133
-
200
'''
n = int(input())

i=0
while True:
    i=i+1
    if int(str(bin(i))[2:])%n == 0:
        print(str(bin(i))[2:])
        break
