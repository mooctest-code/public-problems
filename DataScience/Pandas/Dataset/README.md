---
题目: 加载数据集
简介: 加载 sklearn 中自带的数据集
难度: 1
标签: sklearn-datasets|数据集
作者: 谢子聪
慕码: Unknown
---

### 题目描述

[**scikit-learn**](scikit-learn.org)（sklearn） 是常用的 Python 机器学习库。如下图所示，它可以做非常多的事。

![](https://img-blog.csdnimg.cn/2018111720571969.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1hpYW9ZaV9Fcmlj,size_16,color_FFFFFF,t_70)

这次我们只用它做一件小事。sklearn 自带了一些经典标准数据集的小样本。比如波士顿房价数据集（boston）、鸢尾花数据集（iris）、数字识别数据集（digits）、葡萄酒质量数据集（wine）等等。

使用 `datasets.load_xxx()` 即可加载指定的 xxx 数据集。返回的是一个字典，包括：

| 键            | 描述                                                         |
| ------------- | ------------------------------------------------------------ |
| data          | 特征集，每行为一个数据项，每个数据项为一个特征列表           |
| feature_names | 特征的名称                                                   |
| target        | 预测目标，可能是连续型（用于回归）也可能是分类型（用于分类） |
| target_names  | 目标的名称                                                   |
| DESCR         | 数据集描述                                                   |
| filename      |                                                              |

**任务一：**给定数据集的名称，请你加载该数据集，并输出前三个特征名称和前五个数据项的前三个特征。

[**Pandas** ](https://pandas.pydata.org/) 是常用的 Python 数据分析库，它可以做非常多的事。这次我们也只用它做一件小事：将上述数据集转换成 pandas 的 DataFrame。

**任务二**：使用 DataFrame 的 `head()` 输出上述数据集的前五个数据项的前三个特征。 

### 输入描述

输入为数据集的名称。

### 输出描述

输出任务一、任务二的结果。每个任务前输出一行 `Task x:`，两两任务间加一个空行。任务一每行元素之间使用制表符隔开。

### 测试样例

#### 样例1: 输入-输出

```
wine
```

```
Task 1:
alcohol	malic_acid	ash
14.23	1.71	2.43
13.2	1.78	2.14
13.16	2.36	2.67
14.37	1.95	2.5
13.24	2.59	2.87

Task 2:
   alcohol  malic_acid   ash
0    14.23        1.71  2.43
1    13.20        1.78  2.14
2    13.16        2.36  2.67
3    14.37        1.95  2.50
4    13.24        2.59  2.87
```

### 提示

1. `eval`
2. `DataFrame(data=, columns=)`