'''TESTCASE
1
-
89
-
23
-
14
-
6789
'''


def square(num: int):
    return sum(map(lambda x: int(x)**2, str(num)))


def numsChain(num: int):
    chain = [num, square(num)]
    while chain[-1] not in (1, 89):
        chain.append(square(chain[-1]))
    return chain


num = int(input())
print('->'.join(map(str, numsChain(num))))
