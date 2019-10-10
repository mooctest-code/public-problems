---
题目: 合法的标识符
简介: 自行实现一个判断是否为合法标识符的函数
难度: 1
标签: 字符串
作者: 张莉
慕码: Unknown
---

### 题目描述

字符串有一个 `isidentifier ()` 方法，功能是用来判断给定的字符串是否为合法的标识符。请自行实现此方法的相似功能，完成函数 `checkId()`，判断字符串是否为合法标识符，输出判断结果的信息：

1. 若合法，则输出 'Valid identifier'；
2. 若首字符不合法，则输出 'Error. First char must be alpha or \_'；
3. 若首字母合法其他字符不合法，则输出 'Error. Other chars must be alpha, number or \_ '。

### 输入描述

输入为一个字符串（长度大于 0）

### 输出描述

根据题目描述输出对应信息

### 测试样例

#### 样例1: 输入-输出

```
a1
```

```
Valid identifier
```

#### 样例2: 输入-输出

```
1a
```

```
Error. First char must be alpha or _
```

#### 样例3: 输入-输出

```
a.
```

```
Error. Other chars must be alpha, number or _
```

