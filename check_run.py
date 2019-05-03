from os import path
import subprocess
import json
import sys
import os
import zipfile
import base64
from io import StringIO

"""
Usage:

python ./check_run.py your-problem-folder
# run your solution.py with input

python ./check_run.py your-problem-folder -r
# run your solution.py and write the first testcase into README.md
python ./check_run.py your-problem-folder -r -n
# you can specific number n to write first n testcases into README.md

python ./check_run.py your-problem-folder -z
# run your solution.py and zip your problem to your-problem-folder.zip

python ./check_run.py your-problem-folder -r -z
"""

problem = os.path.normpath(sys.argv[1])

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

silent = '-s' in sys.argv
fromInFile = '-i' in sys.argv
zipProblem = '-z' in sys.argv
replaceTestcase = '-r' in sys.argv

if replaceTestcase:
    ntestcases = 1
    p_r = sys.argv.index('-r')
    if p_r < len(sys.argv)-1 and '-' not in sys.argv[p_r+1]:
        ntestcases = int(sys.argv[p_r+1])

def myprint(str):
    if not silent:
        print(str)

'''
Load solution.py and testcases
'''
testcases = []
myprint('Load solution.py and testcases')
with open(path.join(problem, 'solution.py'), 'r', encoding='utf-8') as f:
    firstline = f.readline() # '''TESTCASE
    if fromInFile or firstline != '\'\'\'TESTCASE\n':
        fromInFile = True
    else:
        testcase = []
        while f.readable():
            line = f.readline()
            if line in ('-\n', '\'\'\'\n'):
                testcases.append(''.join(testcase))
                testcase = []
                if line[0] == '\'':
                    break
            else: testcase.append(line)

    if zipProblem:
        metadata['sourceCode'] = firstline + f.read()


if fromInFile:
    myprint('Load testcases from input file')
    with open(path.join(problem, 'input'), 'r', encoding='utf-8') as f:
        testcases = f.read().split('-\n')
        if testcases[-1] == '':
            testcases = testcases[:-1]
        elif testcases[-1][-1] == '-':
            testcases[-1] = testcases[-1][:-1]

testcases = list(map(lambda x: {"input": x}, testcases))

# if len(testcase) < 2:
#     myprint("Please provide at least two testcases!")
#     sys.exit(0)

'''
Run solution.py
'''
for i in range(len(testcases)):
    runer = subprocess.Popen(['python', path.join(problem, 'solution.py')], stdout=subprocess.PIPE,
        stdin=subprocess.PIPE, stderr=subprocess.STDOUT)

    (stdout, stderr) = runer.communicate(str.encode(testcases[i]['input']))
    if stderr:
        myprint(stderr)
        sys.exit()

    testcases[i]['output'] = bytes.decode(stdout).replace('\r', '')
    
    myprint("Testcase {}:".format(i+1))
    myprint("Input:")
    myprint(testcases[i]['input'])
    myprint("Output:")
    myprint(testcases[i]['output'])

'''
Write testcase into README.md
'''
if replaceTestcase:    
    repl = "### 测试样例\n\n"
    hasInp = 'NoInput' != testcases[0]['input'][:7]
    for i in range(ntestcases):
        repl += ("#### 样例" + str(i+1) + ": " 
            + ("输入-" if hasInp else "") + "输出\n\n"
            + ("```\n" + testcases[i]['input'] + "```\n\n" if hasInp else "")
            + "```\n" + testcases[i]['output'] + '```\n\n')
    
    with open(path.join(problem, 'README.md'), 'r', encoding='utf-8') as f:
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
        myprint("Testcases in README.md has been replaced.")

'''
Generate meta.json and zip file
'''
metadict = {
    '题目': 'title',
    '简介': 'simple_desc',
    '难度': 'difficulty',
    '标签': 'tag',
    '作者': 'author'
}

if zipProblem:
    # read README.md to get title and description
    with open(os.path.join(problem, 'README.md'), 'r', encoding='utf-8') as f:
        cnt = 0
        f.readline()
        for line in f:
            if line == '---\n':
                break
            try:
                metadata[metadict[line[:2]]] = line[4:-1]
            except:
                pass
        f.readline()
        metadata['desc'] = f.read()

    # load template
    try:
        f = open(os.path.join(problem, 'template.py'), 'r')
        metadata['templateCode'] = f.read()
        f.close()
    except Exception: 
        pass

    metadata['testCases'] = testcases

    # write to meta.json
    with open(os.path.join(problem, 'meta.json'), 'w', encoding='utf-8') as w:
        json.dump(metadata, w, ensure_ascii=False, indent=4)
        myprint('meta.json has been written to ' + problem + '/meta.json')

    # zip all files
    with zipfile.ZipFile(problem + '.zip', 'w') as z:
        z.write(os.path.join(problem, 'meta.json'), 'meta.json')
        # public and .mooctest folder
        if os.path.exists(os.path.join(problem, 'workspace')):
            z.write(os.path.join(problem, 'workspace'), 'workspace')

        myprint('zip file has been created to ' + problem + '.zip')

print(problem, 'Done.')