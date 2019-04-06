[y, m, d] = list(map(int, input().split('-')))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
_sum = months[m-1] + d
if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)) and m > 2:
    _sum += 1

print(_sum)