---
题目: 高尔顿钉板
简介: 计算高尔顿钉板概率
难度: 2
标签: 概率分布
作者: 谢子聪
慕码: 3120/1781
---

### 题目描述

![高尔顿钉板](https://i.ytimg.com/vi/oPCcOtQKU8M/hqdefault.jpg)

各位应该都见过如上图所示的装置。小球从上方落下，遇到钉子时会以 0.5 的概率往左或者右方滚下。这种装置是英国生物统计学家高尔顿设计的用来研究随机现象的模型，称为高尔顿钉板。

现有一个具有 n 层钉子的高尔顿钉板，第一层有 1 个钉子，第 n 层有 n 个钉子，假设小球每次落下必碰到钉子，且滚向左右两边的概率均为 0.5，试求小球分别从第 n 层的 n + 1 个空隙落下的概率。比如第二层有三个空隙可落下。

### 输入描述

输入为钉子的层数 n。

### 输出描述

输出小球分别从 n +1 个空隙落下的概率，从左到右，均保留四位小数。

### 测试样例

#### 样例1: 输入-输出

```
1
```

```
0.5000 0.5000
```

#### 样例2: 输入-输出

```
3
```

```
0.1250 0.3750 0.3750 0.1250
```
