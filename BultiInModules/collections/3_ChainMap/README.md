合并配置项

### 题目描述

你使用过 Sublime Text 或者 VS Code 等代码编辑器吗？它们都把配置项分成了默认配置项和用户配置项。如果用户配置了某一项则使用用户的配置，否则使用默认的配置。

很容易想到使用字典先存默认配置再更新用户配置可以完成这个功能。但是如果现在删除了某项用户配置，如何更新呢？从默认配置项中查找？如果现在又加入了一个工作区的配置（工作区配置的优先级大于用户）呢？

请你学习 collections 的 [ChainMap](https://docs.python.org/zh-cn/3/library/collections.html#collections.ChainMap) 和 [OrderedDict](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict)，并使用 ChainMap 来实现多级配置项。

### 输入描述

输入包括五行。

第一到三行分别为默认、用户和工作区的配置项字典。优先级 工作区 > 用户 > 默认。

第四行为一个配置项 i 的键值，第五行为一个配置项 j 的键值。

### 输出描述

输出两行。

第二行为删除配置项 i 后，第 i 项的值。

第三行为删除配置项 j 后，第 j 项的值。

具体输出格式请参考测试样例。

### 测试样例

#### 样例1: 输入-输出

```
{ 'font': 'Consolas', 'autoIndent': True}
{ 'font': 'Hack', 'autoIndent': False}
{ 'autoIndent': True}
autoIndent
autoIndent
```

```
False
True
```

### 说明

本题假设配置项优先从优先级更高的配置开始删除，尽管这不符合实际情况。
