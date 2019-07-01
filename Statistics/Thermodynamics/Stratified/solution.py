'''TESTCASE
iris
-
wine
-
breast_cancer
'''

from sklearn import datasets
import pandas as pd


def stratifiedSample(df: pd.DataFrame) -> pd.DataFrame:
    _min = min(df['target'].value_counts())
    return df.groupby('target').apply(lambda g: g.sample(_min, random_state=0))


dataset = eval('datasets.load_{}()'.format(input()))

feature_names = dataset['feature_names']

df = pd.DataFrame(data=dataset['data'],
                  columns=feature_names)
df['target'] = dataset['target']

print(stratifiedSample(df)[feature_names[:3]].describe())
