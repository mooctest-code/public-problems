class Student:
    def __getattr__(self, name):
        if name == 'info':
            return '\n'.join([
                '姓名: ' + getattr(self, 'name'), 
                '学号: ' + getattr(self, 'sno'), 
                '年级: ' + getattr(self, 'grade')])
        return ''


name, sno, grade = input().split()
student = Student()

# TODO

print(''' TODO ''')