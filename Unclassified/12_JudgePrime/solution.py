def is_prime(a):
    if a < 2: 
        return False
    if a == 2:
        return True
    x = int(a ** 0.5)+1
    for i in range(3, x, 2):
        if a % i == 0:
            return False
    return True

print(is_prime(int(input())))
