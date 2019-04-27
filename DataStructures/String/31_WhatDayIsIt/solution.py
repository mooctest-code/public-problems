'''TESTCASE
Sa
-
Tu
-
th
-
M
-
f
'''
dayOfWeek = ['Sunday', 'Saturday', 'Friday', 'Monday', 'Tuesday', 'Thursday', 'Wednesday']

s = input().lower()

for i in dayOfWeek:
    if i.lower()[0:len(s)] == s:
        print(i)
        break