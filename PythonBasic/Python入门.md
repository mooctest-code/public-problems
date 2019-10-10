# Python快速入门

## 数据对象

#### 数值 int, float, bool

计算器

```python
4 + 3 # 加
4 - 3 # 减
4 / 3 # 除，保留小数部分
4 // 3 # 除，只保留整数部分
4 ** 3 # 幂运算
4 % 3 # 取模
(4 + 3) ** 2 - 1 == 48
```

位运算

```python
~2 # 取反
2 & 3 # 按位与
2 | 3 # 按位或
2 ^ 3 # 按位异或
1 << 2 # 左移运算符
4 >> 1 # 右移运算符
```

赋值

```python
a = 1
b = 2
c = a + b
b += a
c //= b
a, b = b, c # 将 b 的值赋给 a，将 c 的值赋给 b
```

类型

```python
type(1) # 整型 int
type(1.0) # 浮点型 float
type(True) # 布尔型 bool
```

### 字符串 str

赋值

```python
# 单引号
s = 'Hello World'
# Python 没有字符类型，字符实际是长度为 1 的字符串
type('a') == str
# 双引号，与单引号基本等同
d = "Hello World"
# 三引号，写多行
t = """Hello
World
"""
# 在单引号字符串中可以直接使用双引号
sd = 'Hello "World"'
# 在双引号字符串中可以直接使用单引号
ds = "'Hello' World"
# 在三引号字符串中可以直接使用单/双引号
tsd = """'Hello'
"World"
"""
```

常用方法

```python
len(s) # 字符串长度

# 转为大写
# Python 数据对象的内置函数大都不改变原数据，而是返回一个修改后的拷贝，你需要重新赋值
s_upper = s.upper()
(s != s_upper) == True

# 计数，统计输入字符串在原字符串中的出现次数
s.count('o') == 2
s.count('Hello') == 1

s.split(' ') == ['Hello', 'World'] # 分割
''.join((s, d, t)) # 拼接
s.replace('World', 'Python') == 'Hello Python' # 替换
```

运算

```python
s + ' ' + d + ' ' + t == ' '.join((s, d, t))
s * 2 == 'Hello WorldHello World'
```

格式化

```python
# f-string
software, version = 'Python', 3
f'您电脑中的 {software} 当前版本为 {version}'
# format
'您电脑中的 {} 当前版本为 {}'.format(software, version)
# %
'您电脑中的 %s 当前版本为 %d' % (software, version)
```

索引

```python
# 单个字符
s[0] # 一个字符
s[-2] # 倒数第二个字符

# 连续子串 start:stop，不包括 stop 那一位，start 和 stop 可省略
s[3:6] # s[3] 到 s[5]，不包括 s[6]
s[:3] # 前两个字符
s[3:] # 从第三个字符开始到字符串尾

# 间隔子串 start:stop:step
s[3:6:2] # s[3] 和 s[5]
s[::-1] # 通过 step = -1 实现字符串逆序

# 修改子串
s[0] = 'h'
s[3:6] = 'l0+'
```

查找

```python
# 使用 in 查找
'Hello' in s
'Python' not in s
# 使用 find 查找
s.find('Hello')
s.index('e')
```

### 对象 Object

标题使用『数据对象』而不是『数据类型』，是因为 Python 中一切都为对象，之前学习的数值类型还是字符串，都是对象。字符串内置的方法是字符串这个对象的方法 methods。

下面介绍一些内置的对象。

### 列表 list

列表 `[]` 是一序列的对象，意味着你可以装各种数据对象到一个列表中：

```python
l = [1, '1', 'one', [1, '1']] # 使用 [] 初始化列表
```

列表的运算、索引和查找与字符串基本一致：

```python
# 索引
l[0]
l[1:3]
l[1] = 2
l[3][0] = 2 # 索引列表中的列表
# 运算
[1, 2] + ['3', 4] == [1, 2, '3', 4] 
[1, 2] * 2 == [1, 2, 1, 2]
# 查找
'one' in l
'two' not in l
l.index('two') # 当对象不在列表时会报错
```

常用方法

```python
len(l) # 列表大小
[4, 3, 1, 2].sort() # 排序，内部改变原列表，不需要重新赋值，当列表对象间必须可比计较
l.append('two') # 在列表尾增加一个对象
l.extend([3, 'four']) # 拼接一个列表到列表尾
l.remove('one') # 删除，只会删除第一个值相同的对象
l.count(1) # 统计对象出现次数
```

### 元组 tuple

元组可以看作是不可修改的（immutable）列表，元组比列表拥有相对更高的效率。

元组的不可修改是指其对象本身不可修改，但是一些生成新元组的运算是没问题的：

```python
(1, 2) + ('3', (1, 2))
(1, 2) * 3
```

### 集合 set

集合是一个无序的不重复元素序列，得益于其数据结构，它的查询效率远高于列表元组，但它不可存储可变的（mutable）数据对象，也不可通过索引访问。

> 注意这个无序意味着存储相同元素的集合在不同的系统环境上顺序可能不一致

```python
s = {1, 2, 3}
s = set([1, 2, 2, 3])
```

运算符

```python
a = {1, 2, 3}
b = {1, 2}
3 in a # 判断 3 是否在列表
a - b # 得到集合 a 中包含但不在集合 b 中的元素集合
a | b # 得到集合 a 或集合 b 中的元素组成的集合
a & b # 得到集合 a 和 b 中都包含的元素集合
a ^ b # 不同时在集合 a 和 b 中的元素
```

常用方法

```python
# 增加一个数据
s.add(4)
s.update(5)

# 移除一个数据
s.remove(6) # 若不存在会报错
s.discard(6) # 不会报错

s.clear() # 清空

s.difference(a, b) # s 与 a 和 b 的差集
s.intersection(a, b) # 交集
s.isdisjoint(a) # 是否不包含相同元素
s.issubset(a) # 判断 s 是否为 a 的子集
s.issuperset(a) # 判断 s 是否为 a 的超集
s.symmetric_difference(a) # s 和 a 不重复的元素集合
s.union(a, b) # s, a 和 b 的并集
```

## 流程控制

流程控制控制代码执行的顺序。Python 依靠缩进来表示不同的代码块，并通过 `if for while` 等流程控制语句来控制这些代码块的执行：

```python
if a == 1:
    '''代码块
    '''
elif a > 3:
  	'''代码块
  	'''
else:
    '''代码块
    '''
    
while a < 3:
    '''代码块
    '''
    a += 1
```

### 布尔条件

Python 使用 `and`, `or` 来连接多个布尔条件，使用 `not` 表示非。

```python
(a > 3) and (a < 5)
a < 1 or a > 3
not (a < 1)
```

### 条件语句 if elif else

### 循环

#### for

Python 的 for 循环是从可迭代的对象中取出数据对象：

```python
for item in iterable_object:
    do something on item
   
# 打印中的每一个字符
for c in 'hello':
    print(c) 

# 统计列表中类型为字符串的数据对象的个数
cnt = 0
l = ['a', 1, 'one']
for i in l:
    if type(i) == str:
        cnt += 1
# Python 的魅力 - 用一条语句实现：
count = len([0 for i in l if type(i) == str])
count = len(list(filter(lambda x: type(x) == str, l)))
count = list(map(type, l)).count(str)
```

在上述的循环中修改取出的数据对象并不会影响原可迭代对象，我们需要通过索引来修改原对象。Python 提供了 `range` 函数来生成一个可迭代的数字序列，这样我们就可以通过索引得到每一个数据对象：

```python
for i in range(0, len(l)):
  l[i] = 0
  
for i in range(0, 10):
  for j in range(0, 10):
    # do something
```

另一种方式是使用 `enumerate` 为每次循环增加一个计数：

```python
l_types = [0] * len(l)
for i, v in enumerate(l):
    l_types[i] = type(v)
```

#### while

while 循环比较简单，将一直循环直到达到指定条件：

```python
while condition:
    do something
    update condition variable
    
i = 0
while i < len(l):
    l_types[i] = type(l[i])
    i += 1
```

### 遍历字典

遍历字符串、列表、元组和集合的方式基本是一致的，但字典有一点区别：

```python
# 遍历键
for key in d:
		pass
  
# 遍历键值对
for key, v in d.items():
  	pass
```

## 函数

### 全局内置函数

Python 提供了非常多有用的全局内置函数，大体可以分为以下几类：

[Python内置函数详解——总结篇](https://www.cnblogs.com/sesshoumaru/p/6140987.html)

- 数值和字符串
  - 数学运算：abs, divmod, complex, pow, round
  - 编译执行：compile, eval, exec, repr
  - 字符编码：ascii, bytes, bytearray, ord, chr
- 可迭代对象
  - 序列操作：all, any, enumerate, filter, iter, len, map, max, min, range, reversed, slice, sorted, sum, zip
- 类和对象
  - 类型转换：bin, bool, float, int, list, set, str, tuple, format
  - 对象操作：help, dir, id, hash, type, vars
  - 反射操作：isinstance, issubclass, hasattr, getattr, setattr, delattr, callable
  - 装饰器：property, classmethod, staticmethod
- 系统操作
  - 变量操作：globals, locals
  - 交互操作：print, input
  - 文件操作：open

上面这些全局函数都很常用，需要掌握。

### 自定义函数

Python 使用 `def` 关键字定义函数，函数默认返回 None

```python
def none():
		return
  
def get_one():
  	return 1
```

#### 参数

Pyhton 支持多种形式的参数。

```python
# 必选参数
def must_has(a):
		return a is not None
  
# 默认参数
def empty_list(length=0):
  	return [None] * length
  
empty_list()
empty_list(3)
emprt_list(length=4) # 使用键值对传入参数，代码的可解释性更好
  
# 变长参数，将参数存入到 args 元组中
def sum_all(*args):
  return sum(args)

print(sum_all(1, 2, 3))

# 关键字参数
# 可以通过键值对的形式传递参数到参数字典中
def arg_to_dict(**kwargs):
  return kwargs

d = arg_to_dict(a=0, b=[1, 2, 3], c='four')
```

上述这几种参数可以结合在一起使用：

```python
def func1(a, b, c=0, d=1):
  	return
  
func1(1, 2, d=3)

def func2(a, b, **kwargs):
  	return
  
func2(1, 2, c=3, d=4)

def func3(a, b, c=0, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)
    return

func3(1, 2, 3, True, 'one', d=0, e=None)
```

传递参数时必须注意以下几点：

1. 必须按照 必选参数->默认参数->变长参数->关键字参数 的顺序

2. 传入参数时，将优先满足排在前面的参数

3. 在填满必选参数和默认参数后，*args 和 **kwargs 才会生效

4. 在填满必选参数和默认参数后，不能再以键值对的形式修改这些参数

   ```python
   def f(a, b, c=0, **kwargs):
   		return
   		
   f(1, 2, 3, c=4) # error
   ```

5. *args 不会接收键值对形式传入的参数，会报错

   ```python
   def f(a, b, *args):
     	return
     
   f(1, 2, c=0) # error
   ```

6. **kwargs 只接收键值对形式传入的参数

   ```python
   def f(a, b, **kwargs):
   		return
   		
   f(1, 2, 3) # error
   ```

#### * 和 **

之前的例子中出现了  `*` 和 `**` 这两个特别的符号，这两个符号用于解包。`*` 用于解序列，`**` 用于解字典，什么意思呢？举个例子：

```python
def f(a, b, c):
		return

l = [1, 2, 3]

def g(a, b=2, **kwargs)
		return

d = {'a': 3, 'b': 4, 'c': '5'}
```

现在我们希望把 l 中的元素作为参数传入 f 中，把 d 的键值对作为参数传递到 g 中，我们可以这样：

```python
f(*l) # 解包 l --> f(1, 2, 3)
g(**d) # 解包 d --> g(a=3, b=4, c='5')
```

这种解包是非常有用的，比如我们要输出一个列表，但不想输出列表的符号，可以：

```python
print(*l)
```

### 高阶函数

高阶函数是指以函数作为参数的函数：

```python
def add(x, y, f): # add 是一个高阶函数
		return f(x) + f(y)
  
add(1, 2, abs)
```

#### map 和 filter

map 和 filter 是 Python 全局函数，也是常用的高阶函数。

`map(func, iterable)` 用于应用特定函数到一个可迭代对象：

```python
map(abs, [1, -2, 3])
```

`filter(func, iterable)` 用于以特定函数过滤可迭代对象：

```python
filter(isdigit, ['1', 's', '23'])
```

需要注意的是，这两个高阶函数在 Python 3 中返回的分别是 map 和 filter 对象，可以通过类型转换函数，比如 `list()` 转换为需要的数据对象。

### 匿名函数 lambda

匿名函数 `lambda x: do_something_on_x` 常常和高阶函数结合使用

```python
map(lambda x: x*2, [1, -2, 3])
filter(lambda x: type(x) == str, ['1', 123, '23'])
```

当然，有时候直接使用列表生成器其实更方便：

```python
[x*2 for x in [1, -2, 3]]
```

## TODO

- 面向对象
- 常用内置模块

