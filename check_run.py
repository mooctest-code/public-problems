from os import path
import subprocess
import json
import sys

"""
Usage:
python ./check_run.py your-problem-folder

It will generate a testcase.json to your-problem-folder
"""

problem = sys.argv[1]
testcase = []

if '-t' in sys.argv: # from testcase
    print('load testcase from testcase.json')
    with open(path.join(problem, 'testcase.json'), 'r', encoding='utf-8') as f:
        testcase = json.load(f)
else: # from input
    print('load testcase from input file')
    with open(path.join(problem, 'input'), 'r', encoding='utf-8') as f:
        inps = f.read().split('EOF')
        for inp in inps:
            if inp in ('', '\n'):
                continue
            testcase.append({"input": inp.lstrip('\n')})

# select testcase to run
p_s = 0
selected = []
try:
    p_s = sys.argv.index('-s')
    selected = [int(i) for i in sys.argv[p_s+1].split(',')]
except ValueError:
    selected = [i for i in range(len(testcase))]

# generate output
for i in selected:
    inp = testcase[i]['input']
    p = subprocess.Popen(['python', path.join(problem, 'solution.py')], stdout=subprocess.PIPE,
        stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.stdin.write(str.encode(inp))
    result = p.communicate()[0]
    testcase[i]['output'] = bytes.decode(result).replace('\r', '')

    print("Testcase {}:".format(i+1))
    print("Input:")
    print(inp)
    print("Output:")
    print(testcase[i]['output'])

# replace testcase in README.md
try:
    p_r = sys.argv.index('-r')
    ntestcases = 1
    if p_r < len(sys.argv)-1 and '-' not in sys.argv[p_r+1]:
        ntestcases = int(sys.argv[p_r+1])
    
    repl = ""
    with open(path.join(problem, 'README.md'), 'r', encoding='utf-8') as f:
        repl = "### 测试样例\n\n"
        hasInp = 'NoInput' != testcase[0]['input'][:7]
        for i in range(ntestcases):
            repl += ("#### 样例" + str(i+1) + ": " 
                + ("输入-" if hasInp else "") + "输出\n\n"
                + ("```\n" + testcase[i]['input'] + "```\n\n" if hasInp else "")
                + "```\n" + testcase[i]['output'] + '```\n\n')
        
        readme = f.readlines()
        p = -1
        l = len(readme)
        for i in range(0, l):
            if "### 测试样例" in readme[i]:
                p = i
                j = i + 1
                # clean content
                while j < l and '### ' != readme[j][:4]:
                    readme[j] = ''
                    j += 1
                    break
                break
        if p == -1:
            readme.append(repl)
        else: readme[p] = repl

    with open(path.join(problem, 'README.md'), 'w', encoding='utf-8') as fw:
        fw.write(''.join(readme))
        print("Testcases in README.md has been replaced.")
except ValueError:
    pass
# write to testcase.json
with open(path.join(problem, 'testcase.json'), 'w', encoding='utf-8') as out:
    # print(testcase)
    json.dump(testcase, out, ensure_ascii=False, indent=4)

print ('Testcases has been written to ' + problem + '/testcase.json')
