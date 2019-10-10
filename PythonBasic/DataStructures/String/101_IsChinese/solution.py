'''TESTCASE
中
-
a
-
你
-
2
'''

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False
s=input()
print(is_chinese(s))