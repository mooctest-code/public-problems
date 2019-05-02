---
题目: repr和str
简介: 使用 repr 和 str 函数
难度: 2
标签: 内置全局函数|类和对象
作者: 谢子聪
慕码: [1666](http://manage.mooctest.net/case/view/1666)
链接: http://code.mooctest.net/#/exercise/edit/2949/1666
---

### 题目描述

完成 Complex 类中的 \_\_repr\_\_ 和 \_\_str\_\_ 函数，使得题目输出如测试样例所示。

### 输入描述

输入为两个整数 real 和 imag，分别代表复数的实数和虚数部分。

### 输出描述

输出请参考测试样例，分别输出该 Complex 类的实例使用 repr()、str() 和 打印其本身得到的结果。

### 测试样例

#### 样例1: 输入-输出

```
1 2
```

```
1.0 + 2.0j
Complex(real=1.0, imag=2.0)
Complex(real=1.0, imag=2.0)
```

