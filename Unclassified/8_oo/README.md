---
题目: 实训八：面向对象
简介: 实现 Register 和 Teacher 类
难度: 2
标签: 类和对象
作者: MOOCTEST
慕码: Unknown
---

### 描述

小南一个人管理了好多个班级的成绩单，现在依照实例八中的Register类，定义教师类Teacher，Teacher类中包含班级和成绩单Register对象对应的dictionary，以及获取所有班级中成绩大于等于80分的所有同学名单的gte80()。

小南作为一个Teacher类的对象，调用xiaoNan.gte80()，输出所有成绩在80分及以上的学生列表。

### 输入

第一行n，代表一共有多少个班级；

之后的n行输入格式形如：Julia,80;Eve,74;Toney,55

学生与成绩之间通过西文逗号隔开，学生成绩组合之间使用西文分号隔开。

### 输出

所有成绩在80分及以上的学生列表。

### 样例输入

```
3
'Tom',63;'Allen',85
'Adan',97;'Julia',80
'Eve',74;'Toney',55
```

### 样例输出

```
['Allen', 'Adan', 'Julia']
```