from sklearn import datasets
import pandas as pd


def stratifiedSample(df: pd.DataFrame) -> pd.DataFrame:
    # value_counts, groupby
    # sample(n=, random_state=0)
    return  # TODO


dataset = eval('datasets.load_{}()'.format(input()))

feature_names = dataset['feature_names']

df = pd.DataFrame(data=dataset['data'],
                  columns=feature_names)
df['target'] = dataset['target']

print(stratifiedSample(df)[feature_names[:3]].describe())
