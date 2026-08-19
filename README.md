# Python Learning Journey

记录我的 Python 学习过程、每日练习与阶段性项目。

当前学习方式以 **持续练习 + GitHub 记录 + 小项目验证** 为主，在学习基础语法的同时逐步建立编程思维，并为后续数据处理、自动化、工程开发等方向打基础。

---

## 🎯 学习目标

* 系统掌握 Python 基础语法
* 建立基本的程序设计思维
* 熟悉变量、条件、循环、列表、函数等核心知识
* 通过小练习巩固每日学习内容
* 逐步完成能够独立运行的小项目
* 保持 GitHub 持续提交记录
* 后续逐步学习文件处理、模块、异常处理、面向对象等内容

---

## 🛠️ 学习环境

* 操作系统：Windows
* Python：3.12
* 编辑器：Visual Studio Code
* 版本管理：Git
* 代码托管：GitHub

---

## 📚 当前学习进度

| Day     | 学习内容                                       | 状态 |
| ------- | ------------------------------------------ | -- |
| Day 001 | Python 基础、变量、输入输出、基础运算                     | ✅  |
| Day 002 | 条件判断 `if / elif / else`                    | ✅  |
| Day 003 | `for / while / range()`、循环与嵌套循环            | ✅  |
| Day 004 | `while True / break`、`list` 列表、索引、切片、查找与遍历 | ✅  |

---

# Day 001

## 学习内容

* Python 程序基本结构
* `print()`
* 变量
* 基本数据类型
* `input()`
* `int()` / `float()`
* 基础算术运算
* 简单程序编写

## 练习目标

能够完成：

```python
输入
↓
数据转换
↓
计算
↓
输出
```

这一最基础的程序流程。

---

# Day 002

## 学习内容

* `if`
* `elif`
* `else`
* 比较运算
* 条件判断
* 多分支程序
* 用户输入与条件判断结合

## 核心结构

```python
if 条件:
    ...

elif 条件:
    ...

else:
    ...
```

目标是能够根据不同输入执行不同程序逻辑。

---

# Day 003

## 学习内容

* `for`
* `while`
* `range()`
* 循环变量
* 循环计数
* 嵌套循环

## 已完成练习

### `sum_100.py`

使用 `for` 循环计算：

```text
1 + 2 + ... + 100
```

### `table99.py`

使用嵌套循环打印九九乘法表。

### `countdown.py`

实现：

```text
10
9
8
...
1
点火！
```

并练习：

```python
range(start, stop, step)
```

中的负步长。

---

# Day 004

## 学习内容

### 循环控制

* `while True`
* `break`
* 无限循环
* 满足条件后主动退出循环

### 猜数字游戏

完成：

```text
随机生成 1～100 的整数
↓
用户不断猜测
↓
猜大 → 提示“大了”
猜小 → 提示“小了”
猜中 → 输出猜测次数并退出
```

涉及：

```python
import random
random.randint()
while True
break
```

---

## List 列表

学习：

```python
fruits = ["apple", "banana", "orange"]
```

### 已掌握操作

创建列表：

```python
shopping_list = ["milk", "bread", "egg"]
```

读取元素：

```python
shopping_list[0]
```

修改元素：

```python
shopping_list[1] = "apple"
```

添加：

```python
shopping_list.append("apple")
```

删除：

```python
shopping_list.remove("bread")
```

获取长度：

```python
len(shopping_list)
```

遍历：

```python
for item in shopping_list:
    print(item)
```

---

## 索引

正向索引：

```text
0  1  2  3 ...
```

负向索引：

```text
... -3 -2 -1
```

例如：

```python
numbers[-1]
```

表示列表最后一个元素。

---

## 切片

基本结构：

```python
list[start:end]
```

遵循：

> 包含开始位置，不包含结束位置。

例如：

```python
numbers[1:4]
numbers[:3]
numbers[2:]
```

---

## 列表查找

已经学习：

```python
in
not in
```

例如：

```python
if name in students:
    ...
```

获取元素下标：

```python
students.index(name)
```

已经能够组合：

```text
input
+
if / else
+
list
+
in
+
index()
```

完成简单的数据查询程序。

---

## 📂 当前目录结构

```text
python-learning-journey/
│
├── exercises/
│   ├── day001/
│   ├── day002/
│   ├── day003/
│   └── day004/
│
├── notes/
├── projects/
├── .gitignore
└── README.md
```

---

## 🚀 下一步

Python 下一阶段继续学习列表相关操作：

* `sort()`
* `reverse()`
* `min()`
* `max()`
* `sum()`

随后逐步进入：

* 字典 `dict`
* 元组 `tuple`
* 集合 `set`
* 函数
* 文件读写
* 异常处理
* 模块
* 面向对象
* 小型综合项目

---

## 📌 当前学习路线

目前整体学习路线调整为：

```text
Embedded C 为主
        ↓
Python 为辅
        ↓
逐步加入电子与硬件基础
```

Python 不停止学习，但控制每日学习量，以持续练习和巩固为主。

---

## 🔄 Git 学习记录

每个学习日完成后：

```bash
git status
git add .
git commit -m "Complete Python Day XXX"
git push
```

通过 GitHub 持续记录整个学习过程。

---

## ✅ 当前状态

```text
Python Day 001 ✅
Python Day 002 ✅
Python Day 003 ✅
Python Day 004 ✅
```

持续更新中。
