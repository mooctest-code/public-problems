from os import path
import subprocess
import json
import sys
import os
import zipfile
import base64
import argparse
from io import StringIO

"""
run `python run.py -h` for help
"""

argparser = argparse.ArgumentParser()
argparser.add_argument('problem', help='problem folder')
argparser.add_argument('-r', '--replace', type=int, nargs='?', const=1,
                       help='write testcase(s) to README.md')
argparser.add_argument('-z', '--zip', action="store_true",
                       help='zip your problem folder for mooccode')
argparser.add_argument('-i', '--input', action="store_true",
                       help='force to get testcase(s) from input file')
argparser.add_argument('-s', '--silent', action="store_true",
                       help='disable terminal output')
args = argparser.parse_args()

problem = os.path.normpath(args.problem)


def myprint(str):
    if not args.silent:
        print(str)


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

'''
Load solution.py and testcases
'''
testcases = []
fromInFile = args.input
myprint('Load solution.py and testcases')
with open(path.join(problem, 'solution.py'), 'r', encoding='utf-8') as f:
    firstline = f.readline()  # '''TESTCASE
    if not fromInFile and firstline != "'''TESTCASE\n":
        myprint('Not find testcase in solution.py')
        fromInFile = True
    else:
        firstline = ''
        testcase = []
        while f.readable():
            line = f.readline()
            if line in ('-\n', "'''\n"):
                testcases.append(''.join(testcase))
                testcase = []
                if line[0] == '\'':
                    break
            else:
                testcase.append(line)

    if args.zip:
        metadata['sourceCode'] = firstline + f.read()


if fromInFile:
    myprint('Load testcases from input file')
    with open(path.join(problem, 'input'), 'r', encoding='utf-8') as f:
        testcases = f.read().split('-\n')
        if testcases[-1] == '':
            testcases = testcases[:-1]
        elif testcases[-1][-1] == '-':
            testcases[-1] = testcases[-1][:-1]

testcases = [{"input": x} for x in testcases]

# if len(testcase) < 2:
#     myprint("Please provide at least two testcases!")
#     sys.exit(0)

'''
Run solution.py
'''
curpath = os.getcwd()
for i in range(len(testcases)):
    runer = subprocess.Popen(['python', 'solution.py'], cwd=problem, stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE, stderr=subprocess.STDOUT)

    (stdout, stderr) = runer.communicate(str.encode(testcases[i]['input']))
    if stderr:
        myprint(stderr)
        sys.exit()

    testcases[i]['output'] = bytes.decode(stdout).replace('\r', '')

    myprint("Testcase {}:\nInput:\n{}\nOutput:\n{}".format(i+1,
                                                           testcases[i]['input'],
                                                           testcases[i]['output']))

'''
Write testcase into README.md
'''
if args.replace:
    hasInp = 'NoInput' != testcases[0]['input'][:7]

    repl = "### 测试样例\n\n" + ''.join(
        [("#### 样例" + str(i+1) + ": "
          + ("输入-" if hasInp else "") + "输出\n\n"
          + ("```\n" + testcases[i]['input'] +
             "```\n\n" if hasInp else "")
          + "```\n" + testcases[i]['output'] + '```\n\n')
         for i in range(args.replace)]
    )

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
        else:
            readme[p] = repl

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

if args.zip:
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
        public_path = os.path.join(problem, 'public')
        if os.path.exists(public_path):
            for i in os.walk(public_path):
                for f in i[2]:
                    z.write(os.path.join(i[0], f), os.path.join(
                        i[0].replace(problem, 'workspace'), f))

        myprint('zip file has been created to ' + problem + '.zip')

print(problem, 'Done.')
