from os import path, listdir
import json
import sys
import subprocess

problems = []
def get_problems(p):
    for i in listdir(p):
        p2 = path.join(p, i)
        if path.isdir(p2):
            if 'meta.json' in listdir(p2):
                problems.append(p2)
            else:
                get_problems(p2)
        
get_problems('.')
problems.remove('./template')
if '-t' in sys.argv:
    problems = ['./template']

cur = {}
with open(path.join('.','probleminfo.csv'), 'r', encoding='utf8') as f:
    f.readline()
    for line in f:
        info = line[:-1].split(',')
        cur[info[-1]] = info[:-1]

probleminfo = []
probleminfo.append(','.join(['题目名', '简单题目描述', '难度', '知识点', '作者', '慕码ID', '题目文件夹']))
for problem in problems:
    # read README.md
    readmepath = path.join(problem, 'README.md')
    meta = []
    readme = None
    with open(readmepath, 'r', encoding='utf-8') as f:
        f.readline() # read '---\n'
        for line in f:
            if line == '---\n':
                break
            meta.append(line[4:-1])

        if problem[2:] in cur:
            curmeta = cur[problem[2:]]
            if meta != curmeta:
                meta = curmeta
                readme = f.read()

    probleminfo.append(','.join(meta + [problem[2:]]))

    if readme: # update meta in README.md
        with open(readmepath, 'w', encoding='utf-8') as f:
            f.write('---\n题目: {}\n简介: {}\n难度: {}\n标签: {}\n作者: {}\n慕码: {}\n---\n'.format(*meta[:6]) + readme)

probleminfo.append('')
with open(path.join('.','probleminfo.csv'), 'w', encoding='utf8') as f:
    f.write('\n'.join(probleminfo))