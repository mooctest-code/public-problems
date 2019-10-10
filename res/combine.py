import json
from os import path

'''
该脚本把题目信息挂到 Python 学习树上，并输出没有出现在学习树上的知识点。

之前前端使用百度脑图来展示知识点和题目，因此需要把题目信息挂到树上，
但之后改成用知识点列表+题目表格的形式，两者解耦了，不再需要将题目信息挂到树上。

因此此脚本目前只用来输出题目信息表格中没有出现在树上的知识点。
'''

cur_dir = path.dirname(__file__)
problem_path = 'probleminfo.csv'
tree_path = 'python_learning_tree.km'

points = {}
with open(path.join(cur_dir, '..', problem_path), 'r', encoding="utf-8") as f:
    f.readline()
    for line in f:
        ps = line.split(',')[3].split('|')
        for p in ps:
            if p not in points:
                points[p] = []
            points[p].append(line)

is_on_tree = set()


def put_problem_to_tree(o, s, dep):
    for i in o['children']:
        tmp = s
        if dep > 0:
            if dep > 1:
                tmp += '-'
            tmp += i['data']['text']

        i['data']['problems'] = []

        for p in points:
            if tmp == p:
                i['data']['problems'] += points[p]
                is_on_tree.add(p)

        if len(i['children']) > 0:
            put_problem_to_tree(i, tmp, dep+1)


def count_problems(o):
    if len(o['children']) == 0:
        o['data']['cnt'] = len(o['data']['problems'])
        o['data']['text'] += ' ' + str(o['data']['cnt'])
        return o['data']['problems']

    ps = []
    if 'problems' in o['data']:
        ps += o['data']['problems']
    for i in o['children']:
        ps += count_problems(i)

    cnt = len(set(ps))
    o['data']['cnt'] = cnt
    o['data']['text'] += ' ' + str(cnt)

    return ps


def pop_problems(o):
    for i in o['children']:
        i['data'].pop('problems')
        if len(i['children']) > 0:
            pop_problems(i)


tree = {}
with open(path.join(cur_dir, tree_path), 'r', encoding="utf-8") as f:
    tree = json.loads(f.read())
    put_problem_to_tree(tree['root'], '', 0)
    count_problems(tree['root'])
    pop_problems(tree['root'])

print('Not in Tree:')
print(set(points.keys()) - is_on_tree)

# with open('./python_learning_tree.km', 'w', encoding='utf-8') as f:
#     json.dump(tree, f, ensure_ascii=False)
