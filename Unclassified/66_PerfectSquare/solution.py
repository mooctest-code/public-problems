a = 100
b = 268

def find():
    x = 1
    while True:
        s1 = int((x+100)**0.5)
        s2 = int((x+268)**0.5)
        if s1 ** 2 == x+100 and s2 ** 2 == x + 268:
            return x
        x += 1

print(find())