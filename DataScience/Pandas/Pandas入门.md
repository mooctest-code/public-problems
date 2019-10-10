## Pandas 入门

Pandas 是 Python 中最常用的数据分析库，它的主要数据结构 Series 和 DataFrame 像数据库中的表一样，每一列数据（属性）都有自己的名称，访问更加容易，并且提供了非常多高效有用的数据统计、聚合分析函数供使用。

[TOC]

### NumPy 入门

NumPy 是 Python 科学计算基本库，是 Pandas 的底层，想要学习 Pandas，有必要先对 NumPy 有一定了解。

```python
import numpy as np
```

`ndarray`（简称 `array` 下称数组），是 NumPy 的主要数据结构，它用来存储多维数据。我们可以使用多种方式来生成一个数组：

- 从列表到数组
- zeros、arange、linspace 等函数生成特定数组
- 使用 np.random 生成随机数组

#### 创建一个随机数组

NumPy 内置了一个随机数生成器 `random`，我们可以使用它来生成随机数组。

```python
np.random.seed(0)
a = np.random.randint(0, 9, (6, 8)) # 6 行 8 列范围在 0 到 9 的随机数组
```

上面代码中第一行 `seed` 用于设置随机数种子，这里涉及到伪随机的概念，这里不做过多解释，简而言之，同个随机数种子，将会产生一样的随机数序列。需要注意的是，它和 Python 的 `random` 库不是一套机制，这两个随机数生成器在相同的种子下并不会产生一样的结果。

#### 属性

ndarray 拥有一些描述属性如大小形状等：

```python
a.shape # 形状（每一维的大小）
a.ndim # 维度
a.size # 大小（数据总数）
a.dtype # 数据类型
a.T # 转置
```

#### 索引

ndarray 使用 [row, column] 的方式索引数据，多维数据同理 [d1. d2. d3. ...]。每一维数据都可以使用和列表、字符串等数据对象一样的 `start:stop:step` 方式来索引多维子数据。

```python
a[1:2, 3:]
a[:, ::-1]
a[a[:, 0, 0] == 6] # 布尔型索引
```

#### 算术运算

可以使用算术运算符为数组中每一个元素进行算术运算：

```python
a + 2
a - 4
a * 3
```

#### 向量运算

为每个元素进行算术运算是很低效的。而向量运算可以大幅提高计算机进行科学计算的效率。NumPy 的底层是 C 语言，ndarray 可以非常快地进行向量运算，即数组与数组之间的运算。

```python
b = np.random.randint(0, 9, (6, 8))
c = np.random.randint(0, 9, (8, 6))
a + b
a * b
a @ c
```

#### 数组重构

```python
ha1, ha2 = np.hsplit(a, 2)
va1, va2, va3 = np.vsplit(a, 3)
np.hstack((ha1, ha2))
np.vstack((va1, va2))
a.flatten()
a.reshape((3, 16))
```

#### 描述性统计

```python
a.max()
a.min()
a.sum()
a.mean()

a.sum(axis=0) # 统计每列的和
a.min(axis=1) # 统计每行的最小值
```

#### 全局函数

```python
np.abs(a)
np.sqrt(a)
np.sum(a)
np.sort(a)
```

#### 比较运算

ndarray 的比较运算将产生一个布尔数组，代表每一个元素参与比较后的结果。

```python
a > 6
np.mean(a > 6) # 取的是 a > 6 产生的布尔数组的平均值
np.sum(a > 3) # a 中值大于 3 的元素个数
# 使用 & 和 | 来组合多个比较运算而不是 and 或 or
(a >= 1) & (a < 3)
(a > 1) | (a < 0)
```

### DataFrame

DataFrame 有三个主要组成部分：索引 index，列 columns 和数据 data。索引标记行，加快行的查找，列名标记列，方便按列索引数据，数据则是类似 NumPy 中的 ndarray。

```python
import pandas as pd
df = pd.DataFrame([[1, 2], [4, 5], [6, 7]], columns=['a', 'b'])
```

```
df:
   a  b
0  1  2
1  4  5
2  6  7
```

上面的 DataFrame 第一列是默认生成的索引列，当然也可以使用指定的列为索引。实际数据有三行两列，a 和 b 是这两列的列名。

#### 类型、属性和方法

DataFrame 主要有以下几种数据类型：

- 数值类型 int, float, bool
- 对象类型 object，字符串、列表、字典等都属于对象类型
- 日期时间 datetime
- 分类类型 category

类似 NumPy，Pandas 的 DataFrame 也有一些描述属性值和描述统计方法

```python
df.dtypes # 每列的类型
df.shape # 形状
df.columns # 列名

df.head(3) # 查看前三行数据

# 下面这些方法会给出每一列的统计
df.describe()
df.mean()
df.max()
df.sum()
```

NumPy 的数值计算也同样适用

```python
df + 3
df + (df / 2)
df > 3
```

### Series

Series 可以看作是只有一列的 DataFrame，DataFrame 大部分的属性和方法也适用于 Series

```python
a = df['a'] # 使用 'a' 索引列，得到的是一个 Series
a.mean()
a.max()
a.value_counts() # 统计 a 中每一个值出现的次数
a.value_counts(normalize=True) # 统计为占比

a + 3
a + (a / 2)
a > 3
```

### 分组 Grouping 和聚合 Aggregating

分组和聚合是数据分析中常用的操作，分组将数据分成多组，聚合将每一组数据进行统计

```python
df.groupby('group column').agg({'agg column': 'agg function'})
# 按照每个年龄进行分组，再计算其他每一列的均值
emp.groupby('age').mean()
# 按照每个年龄进行分组，再聚合计算每个年龄组的薪水平均值
emp.groupby('age').agg({'salary': 'mean'})

def func(df):
  return df
emp.groupby('age').apply(func) # 对每一个分组 apply func

# 按照年龄和性别进行分组，再聚合计算薪水平均值和最大值以及等级的最小值
emp.groupby(['age', 'gender']).agg({'salary': ['mean', 'max'], 'experience': 'min', 'dept': func})
```

另一个常用的聚合分析函数是 pivot_table:

```python
emp.pivot_table(index='age', columns='gender', values='salary', aggfunc='mean')
```

上面函数会生成一个以年龄为索引，性别的每一个分类为列的 DataFrame，数据是每个年龄和性别下的薪水平均值。

### 载入 Scikit-Learn 数据集到 DataFrame

在学习 Pandas 时，我们需要用到 sklearn 自带的经典数据集的小样本如波士顿房价数据集（boston）、鸢尾花数据集（iris）以及数字识别数据集（digits）等。sklearn 中这些数据集使用的是 ndarray 存储，同时附带了一些数据集的描述信息如特征名称、数据集描述等在一个字典中。

| 键            | 描述                                                         |
| ------------- | ------------------------------------------------------------ |
| data          | 特征集，每行为一个数据项，每个数据项为一个特征列表           |
| feature_names | 特征的名称                                                   |
| target        | 预测目标，可能是连续型（用于回归）也可能是分类型（用于分类） |
| target_names  | 目标每个分类的名称                                           |
| DESCR         | 数据集描述                                                   |
| filename      | 数据存储位置                                                 |

我们需要学习如何载入这些数据集到 Pandas 中。

首先，我们先从 sklearn 中得到这些数据：

```python
from sklearn import datasets

iris = datasets.load_iris() # 加载鸢尾花数据集
boston = datasets.load_boston() # 加载波士顿房价数据集
```

得到的是一个字典，里面有上面表格中所说的一些键值对。载入这个数据集到 DataFrame 中非常简单，我们只需要确定数据和列名：

```python
boston_df = pd.DataFrame(data=boston['data'], columns=boston['feature_names'])
# 可以把预测目标也加入到 iris 中方便处理
boston_df['target'] = boston['target']
```

可以写一个更通用的函数：

```python
def from_sklearn(dataset_name, with_target=True):
    dataset = eval(f'datasets.load_{dataset_name}()')
    df = pd.DataFrame(data=dataset['data'], columns=dataset['feature_names'])
    if with_target:
        df['target'] = dataset['target']
    return df
  
boston = from_sklearn('boston')
```

```python
boston.columns:
Index(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT', 'target'],
      dtype='object')
```

### 选择子集

做数据分析，经常需要使用原数据集的子集（部分行和部分列）。Pandas 选择子集的方式有很多，

1. 使用 `[]`，`.loc` 和 `.iloc`
2. 索引 indexing：布尔索引、多索引等
3. 使用函数

#### 轴 axis

Pandas 的多数函数方法都使用 axis 来区分按行和按列，axis=0 代表按列，得到的是每一列的结果，axis=1 代表按行，得到的是每一行的结果。

![1252882-20181130160009588-1393126436](https://img2018.cnblogs.com/blog/1252882/201811/1252882-20181130160009588-1393126436.png)

#### 索引操作 `[]`

三种常用的索引方式：

- 单标签，比如列名和 index
- `start:stop:step`，Python 常见的索引形式
- 列表，比如列名列表，布尔数组等

[] 是非常常见且常用的索引操作，可以根据列名索引列，也可以类似 NumPy 一样使用 `start:stop:step`索引行。

```python
boston[['CRIM', 'ZN', 'RM']] # 索引这三列数据，得到 DataFrame
boston['CRIM'] # 索引一列数据，得到 Series
boston[['CRIM']] # 这样可以得到 DataFrame 而不是 Series

boston[:5] # 前 5 行数据
boston[::2] # 偶数列数据
```

#### 索引器 `.loc`

.loc[row, column] 使用标签（index 和 column name）来索引数据。

```python
boston.loc[100] # 得到 index 为 100 的数据行 Series
# 注意上述的 100 代表的是 index 的值为 100，而不是第 101 行数据
# 若 index 是字符串，则为 boston.loc['xxx'] 
boston.loc[100:102] # 得到 index 从 100 到 102 的数据行
boston.loc[:, 'CRIM'] # 得到 CRIM 列数据
boston.loc[[100, 102], ['CRIM', 'ZN']]
```

.loc 中的 row 和 column 均支持单标签，`start:stop:step` 和列表三种索引方式。

#### 索引器 `.iloc`

和 .loc 不同，.iloc 与 NumPy 的索引方式非常相似：

```python
boston.iloc[1] # 得到第二行数据
boston.iloc[::2, 0] # 得到偶数行和第 0 列数据
boston.iloc[[1, 2], [1, 2]] # 得到 1，2 行和 1，2 列数据
```

#### 索引器 .ix 和索引器的使用建议

.ix 同时支持 .loc 和 .iloc 的索引方式，很方便，但容易混淆，不推荐使用，官方也 deprecated 了。

同样的，[] 索引同时支持行和列以及数字和标签，这也会引起 confuse，比较好的方式是：

- 只用 [] 且 [] 只能用来索引列，且不要使用 dot 来索引列，dot 运算符应该只用来调用 DataFrame 的属性和方法
- 使用 .loc 和 .iloc 来索引行和列，不再使用 .ix

#### 索引 Series

Series 和 DataFrame 一样，支持上述的索引方式，但因为没有多列的概念，因此不支持按列索引。

#### 设置索引

当不指定索引时，DataFrame 会自动创建一个从 0 开始的 `RangeIndex` ，您可以使用 `set_index`自行指定列为索引，比如设置时间为索引，设置名称为索引等。

对索引进行排序后，字符串类型的索引可以通过子串进行索引

```python
df.set_index('name')
df = df.sort_index()
df.loc['A':'B']
```

#### 布尔索引

之前的索引操作和索引器使用的是 index 和列名进行索引，没有使用到数据，而布尔索引则根据数据值来索引数据。布尔索引需要为每一行数据确定是否选择，True 代表选择。

```python
# 在前五个数据中使用布尔索引一些数据
index = [True, False, True, False, False]
boston[:5][index]
boston[:5].loc[index] # 使用 loc 来进行布尔索引而不是 iloc
```

常用的方式是和 Numpy 一样使用比较运算创建布尔索引数组：

```python
boston['TAX'] > 240
boston.loc[(boston['TAX'] > 240) & (boston['ZN'] < 100)]
boston.loc[~(boston['TAX'] > 240) | (boston['ZN'] == 100), 'CRIM']
```

Pandas 提供了一些 `isxxx` 方法来得到布尔索引：

```python
boston['TAX'].isna()
boston['ZN'].isin([100, 200])
boston['TAX'].between(230, 270)
```

#### 赋值

索引出来的数据可以直接赋值，要求是要保持一样的列数，每列可以是一个单值 apply 给所有索引出来的数据，可以是一个具有相同行数的序列

```python
boston['NEW'] = 0
boston.loc[boston['TAX'] > 240, 'NEW'] = 1
boston.loc[:3, ['CRIM', 'ZN']] = [0, 2]
boston.iloc[::2, [0, 3]] = 0
```

#### 尽量避免的索引 - 链式索引

链式索引即在一个索引后接着进行索引：

```python
boston[:100]['ZN']
boston.iloc[:100].loc[:, 'ZN']
```

当第一个索引为切片时，Pandas 将创建一个新的拷贝，在这个新的拷贝上再次进行索引后，之后的操作将不会再改变原数据；而当第一个索引为列时，Pandas 将创建一个 View，在这个 View 上进行索引后，之后的操作将会改变原数据。这样会造成 confuse，应该尽量避免链式索引。

你可以使用 `is_copy` 和 `_is_view` 来判断当前的 DataFrame 是拷贝、视图还是原数据：

```python
boston.is_copy is None
boston._is_view
```

#### 单值索引 `.at` 和 `.iat`

与 .loc/.iloc 类似，但 .at/.iat 只索引一个值。两者的效率相差不大。

### Minimally Sufficient Pandas

Pandas 提供了非常多的属性和方法来访问以及处理数据，可以『条条道路通罗马』。但由于选择太多，很多人在使用 Pandas 会感到困惑：哪一种方式是最佳的？有没有更简单的方法？这些方法之间有什么区别？DunderData 的 Ted Petrou 提出了 [Minimally Sufficient Pandas](https://github.com/tdpetrou/minimally-sufficient-pandas)，指导如何简洁高效地使用 Pandas，写得非常好。

#### 选择子集

这一节前面已经叙述，这里做一些总结：

- 使用 [] 且 [] 只被用来索引列，不要使用 dot 来索引列，dot 应该只被用来访问 DataFrame 的属性和方法
- 使用 .loc 和 .iloc 索引行和列，不再使用 .ix
- 可以使用 .loc/.iloc 代替 .at/.iat，两者在访问单值上效率相距不大
- 避免链式索引，赋值时正确使用原 DataFrame、拷贝和 View，避免 `SettingWithCopyWarning`

#### 重复的方法

##### `read_csv` vs `read_table`

两者的区别只在默认的分隔符，`read_csv` 默认分隔符是逗号，而 `read_table` 默认分隔符是 tab。**推荐只使用 `read_csv`**。

##### `isna` vs `isnull`  和 `notna` vs `notnull`

这两个方式是相同的，因为有 `dropna` 和 `fillna`，为保持一致，**推荐使用 `isna` 和 `notna`** 而不是 `null`。

##### 运算符 vs 运算方法

Pandas 中，每个运算符都有对应的运算方法：

| 运算符 | 运算方法                        |
| ------ | ------------------------------- |
| + -    | add sub/subtract                |
| * /    | mul/multiply div/divide/truediv |
| //     | Floordiv                        |
| **     | pow                             |
| %      | mod                             |
| \> \>= | gt ge                           |
| \< \<= | lt le                           |
| == !=  | eq ne                           |

```python
tax = boston['TAX']
tax_mean, tax_std = tax.mean(), tax.std()
(tax - tax_mean) / tax_std == tax.sub(tax_mean).div(tax_std)
```

在多数情况下，运算符更加简单且直观，但在一些特殊情况下，运算方法能提供更多控制。

**运算符的自动对齐**

Pandas 在进行两个对象（DataFrame/Series）的运算时，会自动进行 `outer join`，当两个对象 index 不匹配时，会产生很多额外的 `na`。

在这种情况下，使用运算方法，可以通过 `fill_value` `axis` 等参数控制运算方向和结果。

##### 内置函数 vs Pandas 方法

Python 内置了一些全局函数如 `sum` `max` 等，这些统计方法在 Pandas 中也有，那么该使用哪个呢？显然，**应该使用 Pandas 内置的方法**，因为 Pandas 的底层 NumPy 使用的是 C 语言来进行这些计算，而 Python 内置的全局函数因为不能确定输入的参数的类型，使用的是迭代每一个数据对象的方式。

#### 标准化 `groupby`

分组和聚合的方式很多，标准化是指只使用一套分组聚合的方式来应对各种分组聚合需求。作者认为的最优的方法是使用 `groupby` + `agg`。

```python
df.groupby('grouping column').agg({'aggregating column': 'aggregating function'})
```

`groupby` 可以使用列名列表一次性分组多个列，`agg` 也可以往字典中添加更多的聚合项。

```python
df.groupby('group column').agg({'agg column': 'agg function'})
# 按照每个年龄进行分组，再计算其他每一列的均值
emp.groupby('age').mean()
# 按照每个年龄进行分组，再聚合计算每个年龄组的薪水平均值
emp.groupby('age').agg({'salary': 'mean'})
# 按照年龄和性别进行分组，再聚合计算薪水平均值和最大值以及等级的最小值
emp.groupby(['age', 'gender']).agg({'salary': ['mean', 'max'], 'experience': 'min'})
```

#### 处理多索引

多索引又称多层索引，在多层索引上进行操作是非常困难的。当你一次对多个列进行分组（产生多个 index），一次性对一个列进行多个聚合操作（产生多层 column）时就会产生。

- 对于多个 index，通过 `reset_index` 只保留一个索引
- 对于多层 column，通过重新命名列来解决，比如上面的 `'salary': ['mean', 'max']` 会产生 `salary | mean max` 这样的双层列，可以重命名为 `salary_mean` 和 `salary_max`。

#### 避免使用 `apply`

apply 方法用于应用自定义的函数到 DataFrame 或 Series 上。apply 方法和循环没有区别，而使用循环还可以一次性进行多个操作，且控制也更自由。能够使用 `apply` 的例子：当 apply 作用于整个列而不是单个数据时。在分组中也应该尽量避免使用 `apply`。

#### `groupby` `pivot_table` 和 `crosstab`

之前章节中介绍过 pivot_table，crosstab 交叉表是特殊的 pivot_table，用于统计行列值相同的元素的出现次数。

```python
# 下面两条语句功能相同
emp.groupby('age').agg({'salary': 'mean'})
emp.pivot_table(index='age', columns='gender', values='salary', aggfunc='mean')
# 下面这条统计的是每个年龄和性别一致的元素的个数
emp.crosstab(index=emp['age'], columns=emp['gender'])
```

#### `melt` `pivot` `stack` 和 `unstack`

- `melt` 汇总多列到 `属性|值` 这样的两列中。

  ```python
  A	B C
  0	a	0
  1 b 1
  
  df.melt(id_vars='A', value_vars=['B', 'C'])
  A	variable	value
  0	B	a
  0 C 0
  1	B	b
  1	C	1
  ```

- `pivot` - un-melting

- `stack` 用列名建立多重索引

  ```
  A
  0	B	a
  	C 0
  1	B	b
  	C	1
  ```

- `unstack` 将多重索引重新恢复成多列

### Mininally Sufficient Guidelines

* 使用同一种方法
* 尽量在内存中操作
* 使用内置函数，尽量避免自定义函数
* 选择数据子集
    * 使用 `[]` 选择列而不是 dot
    * 使用 `loc` 和 `iloc`，不要使用 `ix`
* 重复的方法
    * 对于多个 alias 的方法，只确定使用一种
    * 非特殊情况，使用运算符而不是运算方法
    * 优先使用 Pandas 内置方法而不是 Python 全局函数
* 避免使用 `apply`
* 标准化 `groupby`
    * 三个组件
        * 分组的列
        * 聚合的列
        * 聚合函数
    * 推荐使用 `df.groupby('grouping columns').agg({'aggregating column': 'aggregating function'})`
* 处理多索引
    * 对于多 index，使用 `reset_index`
    * 对于多层 column，重命名列
* groupby, pivot_table, crosstab
* melt, pivot, stack, unstack

**Pandas 中常用的、覆盖大部分功能的属性和方法**：

T、abs、all、any、append、asfreq、astype、clip、columns、copy、corr、count、cov、cummax、cummin、cumprod、cumsum、describe、diff、drop、drop_duplicates、dropna、dtypes、equals、expanding、fillna、groupby、head、idxmax、idxmin、iloc、index、interpolate、isin、isna、loc、max、mean、median、melt、merge、min、mode、nlargest、notna、nsmallest、nunique、pct_change、pivot_table、plot、prod、quantile、rank、rename、replace、resample、reset_index、rolling、round、sample、select_dtypes、shape、shift、sort_index、sort_values、std、sum、tail、to_csv、to_sql、values、var

> TODO: 对这些属性和方法进行分类