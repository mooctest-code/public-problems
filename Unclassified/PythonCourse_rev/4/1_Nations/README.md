---
题目: 国家语言
简介: 使用字典创建国家和语言映射词典，完成相关操作
难度: 3
标签: 字典
作者: 张莉
慕码: Unknown
---

### 题目描述

请根据输入创建一个国家（键）和语言（值）映射的词典 nations，完成如下操作：

1. 显示字典所有的键（所有国家），按国家名的字典序排列；
2. 显示字典所有的值（所有语言），按语言的字典序排列；
3. 显示字典所有的项（所有 `国家-语言` 键值对），按国家名的字典序排列；
4. 获取国家 `France` 对应的语言，如果不存在则输出 `Unknown`；
5. 添加 `{'Spain': 'Spanish', 'Japan': 'Japanese'}` 到该字典中，并输出所有国家，按国家名的字典序排列

### 输入描述

输入第一行为一个整数 N，表示接下来有 N 行输入。

接下来 N 行每行为两个字符串 Nation 和 Language，分别为一个国家（键）和其使用的语言（值），两两间用空格隔开。

### 输出描述

输出请参考题目描述和测试样例，每个操作输出一行。

### 测试样例

#### 样例1: 输入-输出

```
3
China Chinese
USA English
France French
```

```
China France USA
Chinese English French
China-Chinese France-French USA-English
French
China France Japan Spain USA
```

