n = int(input())

i=0
while True:
    i=i+1
    if int(str(bin(i))[2:])%n == 0:
        print(str(bin(i))[2:])
        break
