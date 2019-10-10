def find_QQ(QQ: dict, name: str):
    # 从字典 QQ 中查找姓名为 name 的人的 QQ 号并返回
    # 不存在则返回 None
    return None


def find_luckyguys(QQ: dict):
    # 从字典 QQ 中查找所有拥有 QQ 靓号（5位数或小于5位数）的人的姓名
    # 返回这些人的姓名列表，按字典序排列
    return []


n = int(input())
QQ = {}
for i in range(n):
    qq, name = input().split()
    QQ[name] = qq

name = input()

qq = find_QQ(QQ, name)
luckyguys = find_luckyguys(QQ)
