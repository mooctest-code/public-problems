'''TESTCASE
1.70 62.4
-
1.63 49.6
-
1.83 84
-
1.54 43.3
'''


class BMI:
    def __init__(self, height, weight):
        self.bmi = weight / (height ** 2)

    def printBMI(self):
        print('BMI: {:.1f}'.format(self.bmi))


height, weight = map(float, input().split())

bmi = BMI(height, weight)
bmi.printBMI()
