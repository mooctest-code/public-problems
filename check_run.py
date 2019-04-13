from os import path
import subprocess
import json
import sys
import os
import zipfile
import base64

"""
Usage:
python ./check_run.py your-problem-folder

It will generate a testcase.json to your-problem-folder
"""

problem = os.path.normpath(sys.argv[1])
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
if '-z' in sys.argv or '-r' in sys.argv:
    ntestcases = 1
    if '-r' in sys.argv:
        p_r = sys.argv.index('-r')
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
            if "###" in readme[i] and "测试样例" in readme[i]:
                p = i
                j = i + 1
                # clean content
                while j < l:
                    if readme[j][:3] == '###':
                        if readme[j][3] != '#':
                            break
                    readme[j] = ''
                    j += 1
                break
        if p == -1:
            readme.append(repl)
        else: readme[p] = repl

    with open(path.join(problem, 'README.md'), 'w', encoding='utf-8') as fw:
        fw.write(''.join(readme))
        print("Testcases in README.md has been replaced.")

# write to testcase.json
with open(path.join(problem, 'testcase.json'), 'w', encoding='utf-8') as out:
    # print(testcase)
    json.dump(testcase, out, ensure_ascii=False, indent=4)

print ('Testcases has been written to ' + problem + '/testcase.json')


if '-z' in sys.argv:
    """
    Usage:
    python zip_gen.py yourProblemFolder
    """

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

    template = 'template'

    # read README.md to get title and description
    with open(os.path.join(problem, 'README.md'), 'r', encoding='utf-8') as f:
        metadata['title'] = f.readline().replace('\n', '')
        f.readline() # empty line
        metadata['desc'] = f.read()

    """base64 version
    # load templateCode from template.py
    try:
        f = open(os.path.join(problem, 'problem.py'), 'rb')
        metadata['templateCode'] = bytes.decode(base64.b64encode(f.read()))
        f.close()
    except Exception:
        pass

    # load sourceCode from solution.py
    with open(os.path.join(problem, 'solution.py'), 'rb') as f:
        metadata['sourceCode'] = bytes.decode(base64.b64encode(f.read()))
    """

    # load template
    try:
        f = open(os.path.join(problem, 'template.py'), 'r')
        metadata['templateCode'] = f.read()
        f.close()
    except Exception:
        pass

    # load solution
    with open(os.path.join(problem, 'solution.py'), 'r') as f:
        metadata['sourceCode'] = f.read()

    # load testcase from testcase.json
    with open(os.path.join(problem, 'testcase.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)
        metadata['testCases'] = data

    # write to meta.json
    with open(os.path.join(problem, 'meta.json'), 'w', encoding='utf-8') as w:
        json.dump(metadata, w, ensure_ascii=False, indent=4)
        print('meta.json has been written to ' + problem + '/meta.json')

    # zip all files
    with zipfile.ZipFile(problem + '.zip', 'w') as z:
        z.write(os.path.join(problem, 'meta.json'), 'meta.json')
        # public and .mooctest folder
        folders = ['public', '.mooctest']
        for folder in folders:
            if os.path.exists(os.path.join(problem, folder)):
                for i in os.walk(os.path.join(problem, folder)):
                    for f in i[2]:
                        z.write(os.path.join(i[0],f), os.path.join(i[0].replace(problem, 'workspace'), f))

        print('zip file has been created to ' + problem + '.zip')
