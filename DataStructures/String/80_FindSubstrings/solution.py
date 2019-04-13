s1 = input()
s2 = input()

l2 = len(s2)
cnt = 0
for i in range(len(s1)):
    if s1[i:len(s2)+i] == s2:
        cnt += 1

print(cnt)