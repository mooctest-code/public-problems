'''TESTCASE
1.7 62.4
-
1.63 44
-
1.83 97
-
1.7 93.2
-
1.54 58
'''


class BMI:
    def __init__(self, height, weight):
        self.bmi = weight / (height ** 2)

    def printBMI(self):
        print('BMI: {:.1f}'.format(self.bmi))


class ChinaBMI(BMI):
    infos = [
        (18.5, '偏瘦', '低（但其它疾病危险性增加）'),
        (24, '正常', '平均水平'),
        (27, '偏胖', '增加'),
        (30, '肥胖', '中度增加'),
        (100, '重度肥胖', '严重增加'),
    ]

    def printBMI(self):
        bmi = self.bmi
        i = 0
        while bmi >= self.infos[i][0]:
            i += 1
        info = self.infos[i]
        print('BMI指数：{:.1f}，{}，相关疾病发病的危险性：{}'.format(bmi, info[1], info[2]))


height, weight = map(float, input().split())

bmi = ChinaBMI(height, weight)
bmi.printBMI()
