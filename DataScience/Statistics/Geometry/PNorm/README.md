---
题目: P范数
简介: 实现 P-范数 的计算
难度: 2
标签: 数据汇总-P范数
作者: 谢子聪
慕码: 3154/1802
---

### 题目描述

请你实现函数 `pnorm` 计算一组数据的 p 范数。

### 输入描述

输入两行。第一行为一组数，两两间用空格隔开；第二行为 p 表示需要输出的 p 范数。p 可能为数字，也有可能是 `inf` 表示 `∞` 范数。

### 输出描述

输出该组数的 p 范数。

### 测试样例

#### 样例1: 输入-输出

```
4.59 4.06 1.4 2.26 4.7 5.35 6.28 2.23
2
```

```
11.8213
```

#### 样例2: 输入-输出

```
-5.08 -8.85 5.09 -8.44 7.34 5.94 -3.68 2.64
1
```

```
47.0600
```

#### 样例3: 输入-输出

```
-9.71 8.69 0.45 -3.19
inf
```

```
9.7100
```

