---
题目: 角谷猜想
简介: 输出角谷猜想的演算过程
难度: 2
标签: 字符串-格式化|流程控制|数学问题
作者: MOOCTEST
慕码: 1701
---

### 题目描述

角谷静夫是日本的一位著名学者，他提出了一个猜想（称为角谷猜想）：对于一个自然数n，若为偶数则除以2，若为奇数则乘以3加1，得到一个新的自然数后按照之前的两条规则继续演算，若干次后得到的结果必然为1。输入任一正整数，输出演算过程。

### 输入描述

输入为一个正整数 n (0 < n < 100)

### 输出描述

输出多行表示整数 n 的角谷猜想演算过程，格式参照样例输出。

### 测试样例

#### 样例1: 输入-输出

```
10
```

```
10/2=5
5*3+1=16
16/2=8
8/2=4
4/2=2
2/2=1
```

