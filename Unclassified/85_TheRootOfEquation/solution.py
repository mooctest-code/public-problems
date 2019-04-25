t = tuple(map(int, input().split()))

(a, b, c) = t

def my_quadratic(a,b,c):
    d = b*b - 4*a*c
    if d < 0:
        return 'no real solution'
    else:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        if x1 > x2:
            x1, x2 = x2, x1
        if x1 == x2:
            return 'x = {:.1f}'.format(x1)
        else: return 'x1 = {:.1f}, x2 = {:.1f}'.format(x1, x2)

print(my_quadratic(a, b, c))