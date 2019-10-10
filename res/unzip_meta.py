from os import path, listdir
import json
import subprocess

'''
这个脚本用于将 meta.json 转换为 README.md 和 solution.py
'''

problems = []


def get_problems(p):
    for i in listdir(p):
        p2 = path.join(p, i)
        if path.isdir(p2):
            if 'meta.json' in listdir(p2) and 'solution.py' not in listdir(p2):
                problems.append(p2)
            else:
                get_problems(p2)


get_problems('.')
try:
    problems.remove('./template')
except ValueError:
    pass
# problems = ['./template']

metadata = {
    "title": "",
    "desc": "",
    "templateCode": "",
    "sourceCode": "",
    "lang": "Python3",
    "testCases": [{
        "input": "", "output": ""
    }]
}

metatemplate = '''---
题目: ?
简介: 无
难度: 0
标签: 无
作者: 匿名
---
'''

for problem in problems:
    meta = {}
    with open(path.join(problem, 'meta.json'), 'r', encoding='utf8') as f:
        meta = json.load(f)

    code = meta['sourceCode']
    test = ['\'\'\'TESTCASE']
    for i in meta['testCases']:
        test.append(i['input'].rstrip('\n'))
        test.append('-')
    test[-1] = '\'\'\'\n'
    with open(path.join(problem, 'solution.py'), 'w', encoding='utf8') as f:
        f.write('\n'.join(test) + '\n' + code)

    with open(path.join(problem, 'README.md'), 'w', encoding='utf8') as f:
        f.write(metatemplate.replace('?', meta['title']) + '\n' + meta['desc'])

    if len(meta['templateCode']) > 0:
        with open(path.join(problem, 'template.py'), 'w', encoding='utf8') as f:
            f.write(meta['templateCode'])
