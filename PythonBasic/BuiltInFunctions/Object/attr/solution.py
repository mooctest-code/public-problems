'''TESTCASE
小明 1632436 大三
-
小红 MF1831900 研一
'''

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

setattr(student, 'name', name)
setattr(student, 'sno', sno)
setattr(student, 'grade', grade)

print(getattr(student, 'info'))
