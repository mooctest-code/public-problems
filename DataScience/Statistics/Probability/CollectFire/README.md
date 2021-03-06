---
题目: 集火
简介: 判断集火是否消灭了目标
难度: 2
标签: 概率-独立性
作者: 谢子聪
慕码: 3098/1767
---

### 题目描述

许多游戏中都有"集火"这一概念，即集中火力在一个目标上以快速消灭目标。现在你和你的队友准备集火在一个目标上，假设已知己方队员的命中率和伤害量和目标的血量，且所有有效攻击都在同一时刻命中到目标上，求目标被消灭的概率。

### 输入描述

输入分为四行。第一行为己方的数量 n（0 < n < 9）；第二行为每个己方队员的命中率；第三行为每个己方队员的伤害量，均为正整数；第四行为一个正整数表示目标的血量。

### 输出描述

输出目标被消灭的概率，结果保留四位小数。

### 测试样例

#### 样例1: 输入-输出

```
4
0.5 0.6 0.4 0.5
60 40 80 60
100
```

```
0.6900
```

#### 样例2: 输入-输出

```
5
0.5 0.6 0.4 0.5 0.4
60 40 80 60 80
100
```

```
0.7900
```
