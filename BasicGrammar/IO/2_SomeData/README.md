---
题目: 读取和输出几个数据
简介: 一行中多个数据的读取和输出
难度: 1
标签: 输入输出|类型转换|字符串-格式化
作者: 谢子聪
慕码: 1517
---

### 题目描述

在上一题中，我们读取和输出了不同类型的数据，但是一行中只有一个数据。如果一行中有多个数据，该如何读取呢，又该如何输出呢？

### 输入描述

> 一般来说，我们会说明“两两间有空格”，如果没有说明，请默认是两两间用空格隔开

包含两行。第一行有两个字符串 `s1 s2`，两两间有一个空格；第二行有三个浮点数 `a b c`，两两间有一个空格。

### 输出描述

输出两行。第一行按 `s2 s1` 输出这两个字符串，两两间用一个空格隔开；第二行按 `c b a` 的顺序输出这三个浮点数，各保留两位小数，两两间用一个空格隔开。

### 测试样例

#### 样例1: 输入-输出

```
Hello World
3.1415 0.618 11.11
```

```
World Hello
11.11 0.62 3.14
```

### 提示

#### Python3

从上一题中应该可以看出，Python3 的 `input()` 读取一行数据为字符串，我们需要再转换为指定的类型。那么这一题中在读取一行数据后我们可以使用 `split()` 以空格为分隔符将字符串分隔为多份，代表多个数据：

```python
s1, s2 = input().split()
```

对于浮点数，在分隔后，我们需要将每一个字符串转为浮点型：

```python
inp = input().split()
a, b, c = float(inp[0]), float(inp[1]), float(inp[2])
```

*上面这种方法有点麻烦，我们会在下一题中介绍更方便的方法。

输入解决了，接下来考虑如何在一行中输出多个用空格隔开的数据。输出两个用空格隔开的字符串很简单：

```python
print(s1, s2)
```

对于浮点数，上一题中我们学习了如何输出一个保留三位小数的浮点数，在这里其实也一样：

```python
print('{:.2f} {:.2f} {:.2f}'.format(a, b, c))
```

#### C

在上一题中，我们为了读取包含空格的字符串，使用了 `gets()` 读取一行数据，而这题中不要读取空格，所以使用 `scanf()` ：

```c
char s1[100], s2[100];
scanf("%s %s", s1, s2);
printf("%s %s\n", s1, s2);
```

读取和输出浮点数也类似：

```c++
double a, b, c;
scanf("%lf %lf %lf", &a, &b, &c);
printf("%.2lf %.2lf %.2lf\n", a, b, c);
```

#### C++

同 C 语言，这次不用读取一行数据，所以使用 `cin` 而不是 `getline()`。

```c++
string s1, s2;
cin >> s1 >> s2;
cout << s1 << " " << s2 << endl;
```

对于浮点数，跟上一题也类似：

```c++
double a, b, c;
cin >> a >> b >> c;
cout.precision(2);
cout << fixed << a << " " << b << " " << c << endl;
```

#### Java

Java 的数据读取和输出机制类似于 C/C++：

```java
Scanner scanner = new Scanner(System.in);

String s1 = scanner.next();
String s2 = scanner.next();
System.out.printf("%s %s\n", s1, s2);

double a = scanner.nextDouble();
double b = scanner.nextDouble();
double c = scanner.nextDouble();
System.out.printf("%.2f %.2f %.2f\n", a, b, c);

scanner.close();
```

