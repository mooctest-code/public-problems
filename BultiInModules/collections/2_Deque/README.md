滑动窗口求区间最大值

### 题目描述

给你一个整数列表，以及窗口大小，请你求出每个滑动窗口中的最大值。

### 输入描述

第一行为一组整数，两两间用空格隔开。

第二行为滑动窗口的大小 k。

### 输出描述

输出每个滑动窗口的最大值，两两间用空格隔开。

### 测试样例

#### 样例1: 输入-输出-解释

```
1 5 4 3 1
3
```

```
5 5 4
```

```
[1 5 4] 3 1 -> 滑动窗口中最大值为 5
1 [5 4 3] 1 -> 滑动窗口中最大值为 5
1 5 [4 3 1] -> 滑动窗口中最大值为 4
因此输出 5 5 4
```

### 提示

请使用 collections 库中的 [deque](<https://docs.python.org/zh-cn/3/library/collections.html#collections.deque>) 完成本题。