n = int(input())
a = list(map(int, input().split()))

min_x = min(a)
max_x = max(a)

def convert(x):
    r = x
    if x == min_x:
        r = max_x
    if x == max_x:
        r = min_x
    return str(r)

print(' '.join(map(convert, a)))