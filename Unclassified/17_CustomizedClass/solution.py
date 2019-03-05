class Student:
    def __init__(self, info):
        [self.num, self.name, self.age, self.dep] = info

    def __str__(self):
        return ', '.join(['num: ' + self.num, 'name: ' + self.name,
            'age: ' + str(self.age), 'dep: ' + self.dep])

    __repr__ = __str__

info = input().split()
student = Student(info)
print(student)