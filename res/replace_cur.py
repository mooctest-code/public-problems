from os import path, listdir
import json

p = '.'
problems = []
for f1 in listdir(p):
    if '.' in f1:
        continue
    if path.isdir(f1):
        p1 = path.join(p, f1)
        for f2 in listdir(p1):
            p2 = path.join(p1, f2)
            if path.isdir(p2):
                problems.append(p2)

for problem in problems:
    readme = []
    with open(path.join(problem, 'README.md'), 'r', encoding='utf-8') as f:
        readme = f.readlines()

    l = len(readme)
    hasin = False
    inps = []
    outs = []
    rl, rr = 0, l-1
    for i in range(l):
        if "### 样例输入" in readme[i] or "### Sample Input" in readme[i]:
            rl = i
            j = i+1
            while j < l:
                if "###" in readme[j]:
                    break
                if "```" in readme[j]:
                    for k in range(j+1, l):
                        if "```" in readme[k]:
                            inps.append(''.join(readme[j+1:k]))
                            j = k
                            break
                j += 1
            break

    for i in range(l):
        if "### 样例输出" in readme[i] or "### Sample Input" in readme[i]:
            if rl == 0:
                rl = i
            j = i+1
            while j < l:
                if "###" in readme[j]:
                    rr = j-1
                    break
                if "```" in readme[j]:
                    for k in range(j+1, l):
                        if "```" in readme[k]:
                            outs.append(''.join(readme[j+1:k]))
                            j = k
                            break
                j += 1
            break

    if outs:
        for i in range(rl, rr+1):
            readme[i] = ''
        replace = "### 测试样例\n\n"
        temp = ": " + ("输入-" if inps else "") + "输出\n\n"
        for i in range(len(outs)):
            replace += ("#### 样例" + str(i+1) + temp
                    + ('```\n' + inps[i] + '```\n\n' if inps else '')
                    + "```\n" + outs[i] + "```\n\n")
        readme[rl] = replace
    
    with open(path.join(problem, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(''.join(readme))
