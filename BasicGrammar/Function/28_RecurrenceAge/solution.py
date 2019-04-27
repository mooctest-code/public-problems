'''TESTCASE
None
'''
def age(n):
    return 10 if not n-1 else age(n-1)+2
print(age(5))