[a, b, c, d] = list(map(int, input().split()))

A = (a+c) // 2
B = c - A
C = d - B

print('{} {} {}'.format(A, B, C)) if B - C == b else print(None)