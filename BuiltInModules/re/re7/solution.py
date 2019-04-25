def match( s, pattern):
    if len(s) == 0 and len(pattern) == 0:
        return True
    elif len(s) != 0 and len(pattern) == 0:
        return False
    elif len(s) == 0 and len(pattern) != 0:
        if len(pattern) > 1 and pattern[1] == '*':
            return match(s, pattern[2:])
        else:
            return False
    else:
        if len(pattern) > 1 and pattern[1] == '*':
            if s[0] != pattern[0] and pattern[0] != '.':
                return match(s, pattern[2:])
            else:
                return match(s, pattern[2:]) or match(s[1:], pattern[2:]) or match(s[1:], pattern)
        else:
            if s[0] == pattern[0] or pattern[0] == '.':
                return match(s[1:], pattern[1:])
            else:
                return False
num = int(input())
for i in range(num):
    s = input()
    pattern = input()
    print(match(s,pattern))