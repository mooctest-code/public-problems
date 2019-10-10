# 编程社区出题向导

## 当前情况

您可以通过 [题目信息表格](probleminfo.csv) 和 [Python 学习路线图](https://xxxzc.github.io/fds/#/resources) 查看当前的题目列表以及知识点分布。

我们的题目将发布到 [code.mooctest.net](http://code.mooctest.net) 上。

### 题库说明

```
template/ 出题模版
PythonBasic/ Python基础
	BasicGrammar/ 基础语法题，包括输入输出、变量和运算符、流程控制和面向对象
	DataStructures/ 数据结构题，包括Python内置的数据结构和常用的数据结构
	BuiltInFunctions/ 内置全局函数题
	BuiltInModules/ 内置模块题，包括一些常用内置模块的使用
Algorithms/ 算法题，使用 Python 实现的一些算法
DataScience/ 数据科学
	Statistics/ 概率统计题，数据科学基础课程配套题，详见文件夹中的 README.md
	NumPy/ NumPy 相关题目
	Pandas/ Pandas 相关题目（待出）
	
Unclassified/ 未分类的题目

probleminfo.csv 题目信息表格
run.py 题目测试和打包脚本
gen_info.py 用于生成题目信息表格以及从表格更新信息到题目的 README
res/ 一些资源文件，其中的 .km 文件是思维导图，需要使用百度脑图打开
```

[百度脑图桌面版](https://github.com/NaoTu/DesktopNaotu)

### 题目信息表格

题目信息表格包含如下信息：

`题目名`  `简单题目描述`  `难度 ` `知识点`  `作者`  `慕码ID`  `题目文件夹`

其中：

- `难度` 为 1~5 的整数。1、2 为简单，3、4 为中等，5 为困难

- `知识点` 为完成这道题主要使用到的知识，可能有多个，使用 `|` 隔开。每个知识点可能有两级，比如`字符串-格式化`

- `慕码ID` 为题目的 ID。
1. 如果为一个数字，如 `1234` ，则表示是 [慕码教务管理平台](http://manage.mooctest.net/) 上的一个`测试案例ID`，您可以通过 `manage.mooctest.net/case/view/` + `测试案例ID` 来访问这个测试案例。
  
2. 如果形式如 `1234/5678`，则表示是 [慕码编程平台]() 上的一道题  `试卷/测试案例ID` ，您可以通过 `code.mooctest.net/#/exercise/edit/` + `试卷/测试案例ID`。
  
3. 上面 `试卷/测试案例ID` 中的 `测试案例ID` 也可以通过 1 中的方式访问。
  
- `题目文件夹` 为该题在本题库中的存储位置。

## 参与进来

欢迎您提 issue。

### 1. 出新题目

出题方式和格式要求请参阅 [出题方式.md](%E5%87%BA%E9%A2%98%E6%96%B9%E5%BC%8F.md)（最好自然是直接把题目出好提 issue。直接发链接、题目描述和知识点也是可以接受的）。

### 2. 改进 Python 学习路线图

该路线图目前为个人整理，肯定有遗漏、不合理和错误的分支，欢迎提出来。

### 3. 改进题目信息表格

如果您对题目信息表格有什么建议或者意见，比如某道题是不是还涉及其他知识点、难度定义是不是合理等等，都可以提出来。

### 4. 改进现有题目和出题方式

如果您觉得现有的题目和出题方式在描述、做法或者数据上有什么不合理的地方，也请指出来。