'''TESTCASE
I am a student.
-
Hello Python
-
Hello World!
-
Madam I'm Adam
'''
a = ord('a')
z = ord('z')
cnt = [0 for i in range(z-a+1)]
for i in input().lower():
    if i.isalpha():
        cnt[ord(i)-a] += 1

print(*cnt)
