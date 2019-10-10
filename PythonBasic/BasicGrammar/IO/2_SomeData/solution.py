'''TESTCASE
Hello World
3.1415 0.618 11.11
-
Hello Python
123.456 -123.456 0 
-
Hello C/C++
7.54343 32.8626 32.652523
'''
print(*input().split()[::-1])
print(*map(lambda x: '{:.2f}'.format(float(x)), input().split()[::-1]))