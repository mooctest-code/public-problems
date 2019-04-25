自定义列表

### 题目描述

请学习 collections 的 [UserList](https://docs.python.org/zh-cn/3/library/collections.html#collections.UserList) 并实现一个自动扩展的列表类，当访问下标超过列表长度时，自动扩展列表长度，扩展的数据使用 0 代替。

### 输入描述

第一行为一个初始整数列表 L。

第二行为两个整数 i 和 x，分别表示需要插入的下标和需要插入的数据。

第三行为一个整数 j，表示需要访问的下标。

### 输出描述

输出分为两行。

第一行为在列表第 i+1 项放入 x 后的列表。

第二行为列表第 j+1 项的值。

### 测试样例

#### 样例1: 输入-输出-解释

```
[0, 1]
4 2
3
```

```
[0, 1, 0, 0, 2]
0
```

```
L = [0, 1]，现在需要设置 L[4] = 2，那么你的列表将自动扩展为 L = [0, 1, 0, 0, 2]。
```
