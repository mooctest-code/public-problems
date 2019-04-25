zip函数的应用

### 题目描述
对于给定的列表，前一个元素是后一个元素的师父，输出所有的师徒关系的元组对。

### 输入描述
输入为名字列表，名字之间用逗号隔开

### 输出描述
输出所有的师徒关系的元组，之间换行

### 测试样例

#### 样例1: 输入-输出

```
grandgrandfather,grandfather,father,son,grandson
```

```
('grandgrandfather', 'grandfather')
('grandfather', 'father')
('father', 'son')
('son', 'grandson')
```


