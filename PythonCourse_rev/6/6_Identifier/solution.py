'''TESTCASE
a1
-
1a
-
a.
-
_1a
-
~a
'''


def checkId(s: str):
    if s.isidentifier():
        return 'Valid identifier'
    else:
        if s[0].isalpha() or s[0] == '_':
            return 'Error. Other chars must be alpha, number or _'
        else:
            return 'Error. First char must be alpha or _'


print(checkId(input()))
