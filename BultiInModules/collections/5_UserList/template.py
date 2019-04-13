from collections import UserList

class AutoList(UserList):

    def __setitem__(self, i, item):
        # TODO

    def __getitem__(self, i):
        # TODO

L = AutoList(eval(input()))
i, x = map(int, input().split())
L[i] = x
print(L)
print(L[int(input())])