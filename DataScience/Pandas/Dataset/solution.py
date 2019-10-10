'''TESTCASE
wine
-
boston
-
iris
-
breast_cancer
'''

from sklearn import datasets
import pandas as pd

name = input()

dataset = eval('datasets.load_' + name + '()')
feature_names = dataset['feature_names']
data = dataset['data']

print('Task 1:')
print(*feature_names[:3], sep='\t')
for item in data[:5]:
    print(*item[:3], sep='\t')

print()

df = pd.DataFrame(data=data, columns=feature_names)

print('Task 2:')
print(df[feature_names[:3]].head())
