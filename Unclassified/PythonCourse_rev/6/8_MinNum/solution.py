'''TESTCASE
1 3 0 5
-
4 3 2 1
-
5 3 2 4 0 0
-
1 4 0 4 2
-
0 0 0 0
'''


def minNum(*nums):
    # 参数 nums 为一组数字
    # 返回能够组成的最小数字
    nums = sorted(map(str, nums))
    i = 0
    while i < len(nums) and nums[i] == '0':
        i += 1
    if i < len(nums):
        nums[0], nums[i] = nums[i], nums[0]
    return int(''.join(nums))


print(minNum(*map(int, input().split())))
