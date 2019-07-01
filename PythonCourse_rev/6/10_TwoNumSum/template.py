def twonumSum(l: list, n: int):
    # l 为有序整数列表，n 为目标两个数的和
    # 返回 l 中和为 n 的两个数的下标
    # 返回一组即可且要求其中的一个数尽量小
    return None


l = list(map(int, input().split()))
n = int(input())

twonum = twonumSum(l, n)
print(*twonum) if twonum else print('Not Found')
