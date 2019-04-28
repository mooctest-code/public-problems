from os import path, listdir
import json
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
# problems = ['./template']

old = {}
with open(path.join('res','probleminfo.csv'), 'r', encoding='utf8') as f:
    for line in f:
        info = line[:-1].split(',')
        old[info[5]] = info[6:]

probleminfo = []
for problem in problems:
    with open(path.join(problem, 'meta.json'), 'r', encoding='utf8') as f:
        meta = json.load(f)
        if 'difficulty' not in meta:
            info = [meta['title'], '简单题目描述', '0', '知识点', '匿名', problem[2:]]
        else:
            info = [
                meta['title'], meta['difficulty'], 
                meta['simple_desc'], meta['tag'], 
                meta['author'], problem[2:]]
        
        old_info = old.get(problem[2:], ['0', 'null'])
        probleminfo.append(','.join(info + old_info))

with open(path.join('res','probleminfo.csv'), 'w', encoding='utf8') as f:
    f.write('\n'.join(probleminfo))