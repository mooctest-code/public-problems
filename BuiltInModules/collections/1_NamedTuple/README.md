---
题目: 我也想拥有姓名
简介: 命名元组的使用
难度: 2
标签: collections-namedtuple|命名元组
作者: 谢子聪
慕码: Unknown
链接: Unknown
---

### 题目描述

现在有一个 (x, y) 点坐标需要存储，你会采取什么方式？

- 元组：简单高效但是元素没有名称
- 字典：开销大
- 对象：编写麻烦

有更好的方式吗？那就是 collections 库中的 [namedtuple](<https://docs.python.org/zh-cn/3/library/collections.html#collections.namedtuple>)。可以让元组本身和其元素拥有姓名。

请学习 namedtuple 的使用并完成本题。

### 输入描述

输入为两个整数 x 和 y。 

### 输出描述

请将 namedtuple 命名为 Point，其有两个属性值，分别为 x 和 y。直接使用命名元组输出这个坐标。

### 测试样例

#### 样例1: 输入-输出

```
1 2
```

```
Point(x=1, y=2)
```

