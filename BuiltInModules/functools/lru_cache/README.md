---
题目: lru_cache
简介: 使用 lru_cache 实现动态编程
难度: 1
标签: functools-lru_cache
作者: 谢子聪
慕码: Unknown
---

### 题目描述

各位都知道，递归可能会产生重复的计算，从而影响程序的运行效率，那么该如何改善呢？

请阅读 [functools.lru_cache](https://docs.python.org/zh-cn/3/library/functools.html#functools.lru_cache)，为斐波那契函数 fib() 设计一个合理且足够大的缓存大小，使得该程序的输出如样例所示。

### 输入描述

输入为一个整数 n(0 < n < 20)，表示要得到第 n 位的斐波那契数

### 输出描述

输出为该 fib() 函数的命中情况

### 测试样例

#### 样例1: 输入-输出

```
3
```

```
Hits: 1
```

#### 样例2: 输入-输出

```
5
```

```
Hits: 3
```

