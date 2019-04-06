def oct2dec(o):
    d = 0
    b = 1
    for i in o[::-1]:
        n = int(i)
        if n > 7: return('Invalid octal number!')
        d += b * n
        b *= 8
    return d

o = input()

print(oct2dec(o))