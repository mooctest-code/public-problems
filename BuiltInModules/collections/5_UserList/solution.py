from collections import UserList

class AutoList(UserList):

    def __setitem__(self, i, item):
        if i >= len(self.data):
            self.data += [0] * (i - len(self.data) + 1)
        self.data[i] = item

    def __getitem__(self, i):
        if i < len(self.data):
            return self.data[i]
        else: return 0

L = AutoList(eval(input()))
i, x = map(int, input().split())
L[i] = x
print(L)
print(L[int(input())])