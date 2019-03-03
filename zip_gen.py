# -*- coding: utf-8 -*-

import sys
import os
import zipfile
import base64
import json

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

# problem path
problem = os.path.normpath(sys.argv[1])
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
