'''TESTCASE
3
123456 xiaoming
12345 xiaohong
1234 xiaoli
xiaohong
-
1
123456 xiaoming
xiaohong
-
4
123456 xiaoming
12345 xiaohong
1234 xiaoli
42398 damao
xiaomao
-
1
123456 xiaoming
xiaoming
'''


def find_QQ(QQ: dict, name: str):
    # 从字典 QQ 中查找姓名为 name 的人的 QQ 号并返回
    # 不存在则返回 None
    return QQ.get(name, None)


def find_luckyguys(QQ: dict):
    # 从字典 QQ 中查找所有拥有 QQ 靓号（5位数或小于5位数）的人的姓名
    # 返回这些人的姓名列表，按字典序排列
    return sorted(map(lambda x: x[0],
                      filter(lambda x: len(x[1]) < 6,
                             QQ.items())))


def found(x):
    if not x:
        print('Not Found')
    return bool(x)


n = int(input())
QQ = {}
for i in range(n):
    qq, name = input().split()
    QQ[name] = qq

name = input()
qq = find_QQ(QQ, name)
luckyguys = find_luckyguys(QQ)

if found(qq):
    print(name + '\'s QQ is', qq)

if found(luckyguys):
    print('Lucky guys:', ' '.join(luckyguys))
