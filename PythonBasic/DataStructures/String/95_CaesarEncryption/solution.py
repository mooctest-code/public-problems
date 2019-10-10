'''TESTCASE
MJQQT BTWQI
-
UDYMTS
-
IFSLJW
-
UWTGQJR
'''
s = input()
s = list(s)
for i in range(len(s)):
    if not s[i].isalpha():
        continue
    s[i] = chr(ord(s[i]) - 5) if s[i] > 'E' else chr(ord('V')+ord(s[i])-ord('A'))

print(''.join(s))