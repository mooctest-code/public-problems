from collections import Counter

filepath = input()
dirpath = __file__.split('/')[0:-1]
dirpath.append(filepath)

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

with open('/'.join(dirpath), encoding="utf-8") as f:
    print(Counter(filter(is_chinese, f.read())).most_common(1)[0][0])