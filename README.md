# Python Learning Journey

这是我的 Python 学习与实践仓库。

**开始时间：2026-08-14**

当前职业学习方向已调整为：

> **嵌入式 / 板级硬件工程师**

因此 Python 不再作为主要开发语言深入学习，而是定位为：

> **硬件开发、数据采集、测试自动化和数据分析的辅助工具。**

---

## 学习目标

### 基础阶段

掌握完成硬件辅助开发所需的 Python 基础：

* 变量与基本数据类型
* 输入与输出
* 条件判断
* `for / while` 循环
* `list / tuple / dict`
* 函数
* 模块
* 文件读写
* 异常处理
* CSV
* 基础 Matplotlib

### 后续应用阶段

重点将 Python 用于：

```text
STM32 / 传感器
        ↓
      UART
        ↓
      Python
        ↓
 ┌──────┼──────┐
 ↓      ↓      ↓
CSV   Plot   Test
存储   绘图   自动化
```

最终能够独立编写：

```text
serial_logger.py
    串口数据采集 → CSV

plot_sensor.py
    传感器数据 → 曲线

realtime_plot.py
    串口数据 → 实时绘图

test_report.py
    测试数据 → 自动整理
```

---

## 学习资料

主要参考：

* `jackfrued/Python-100-Days`
* Python 官方文档

开发工具：

* Python 3.12.10
* VS Code
* Git
* GitHub
* Codex / ChatGPT

AI 主要用于：

* 解释代码
* 分析报错
* 提供提示
* 检查练习

尽量避免直接使用 AI 代写完整练习。

---

## 仓库结构

```text
python-learning-journey/
├── notes/          # 每日学习笔记
├── exercises/      # 每日 Python 练习
│   ├── day001/
│   ├── day002/
│   ├── day003/
│   └── ...
├── projects/       # 阶段应用项目
├── .gitignore
└── README.md
```

---

## 当前学习进度

| Day     | 学习内容                            | 状态 |
| ------- | ------------------------------- | -- |
| Day 001 | 环境、变量、数据类型、输入输出、类型转换            | ✅  |
| Day 002 | 比较运算、逻辑运算、`if / elif / else`    | ✅  |
| Day 003 | `for / while / range()`、循环与嵌套循环 | ⏳  |
| Day 004 | `list` 列表                       | ⬜  |
| Day 005 | `dict / tuple`                  | ⬜  |
| Day 006 | 函数                              | ⬜  |
| Day 007 | 模块                              | ⬜  |
| Day 008 | 文件读写                            | ⬜  |
| Day 009 | 异常处理                            | ⬜  |
| Day 010 | CSV 数据处理                        | ⬜  |
| Day 011 | Matplotlib 基础绘图                 | ⬜  |
| Day 012 | Python 基础综合练习                   | ⬜  |

---

## Day 001

已掌握：

* Python 运行环境
* `print()`
* 变量
* `int`
* `float`
* `str`
* `bool`
* `type()`
* `input()`
* 类型转换
* f-string
* 基础数学运算
* `ValueError` 基础排查

已完成：

```text
hello.py
basics.py
input_demo.py
personal_info.py
next_age.py
rectangle.py
temperature.py
bmi.py
```

---

## Day 002

已学习：

```text
>
<
>=
<=
==
!=

if
elif
else

and
or
not
```

能够根据不同条件控制程序执行不同逻辑。

---

## Day 003

当前学习：

```text
for
while
range()
循环变量
累加
倒序循环
嵌套循环
```

当前练习：

```text
sum_100.py
    for循环求 1 + 2 + ... + 100

table99.py
    双重for循环打印九九乘法表

countdown.py
    使用range负步长完成倒计时
```

重点理解：

```python
range(start, stop, step)
```

以及：

```python
total += i
```

等价于：

```python
total = total + i
```

---

## Python 基础阶段路线

```text
变量 / 数据类型
        ✅
        ↓
条件判断
        ✅
        ↓
循环
        ⏳
        ↓
list / dict / tuple
        ↓
函数
        ↓
模块
        ↓
文件
        ↓
异常处理
        ↓
CSV
        ↓
Matplotlib
        ↓
Python基础阶段结束
```

基础阶段结束后，不继续系统深入 Web、爬虫或复杂 Python 工程化内容。

---

## Python × 硬件路线

后续 Python 学习直接服务于硬件主线：

```text
Python基础
    ↓
文件 / CSV
    ↓
pyserial
    ↓
串口读取
    ↓
STM32数据采集
    ↓
CSV保存
    ↓
Matplotlib绘图
    ↓
实时数据显示
    ↓
测试自动化
    ↓
多参数采集系统上位机
```

---

## 暂不学习

当前阶段暂不投入时间学习：

```text
Django
Flask
FastAPI
Web开发
复杂爬虫
异步编程
复杂OOP
机器学习框架
高级Python工程化
```

需要时再按项目需求补充。

---

## 与 C / 硬件学习的关系

当前整体优先级：

```text
C语言 / Embedded C
        ↓
电子与电路基础
        ↓
STM32
        ↓
接口与传感器
        ↓
PCB / 仪器 / Debug
        ↓
完整硬件项目

Python
   └────────→ 数据采集 / 绘图 / 自动测试 / 上位机
```

Python 是工具，C 和硬件开发是当前主线。

---

## 最终 Python 验收目标

基础阶段结束时，应能够：

* 独立阅读基础 Python 程序
* 使用条件和循环完成简单逻辑
* 使用列表和字典处理数据
* 自己编写函数
* 读取和写入文件
* 处理基础异常
* 读取和生成 CSV
* 使用 Matplotlib 绘制实验数据
* 根据文档安装并使用第三方库

硬件应用阶段进一步完成：

* [ ] `serial_logger.py`
* [ ] `plot_sensor.py`
* [ ] `realtime_plot.py`
* [ ] `test_report.py`

---

## 每日学习流程

```text
学习一个知识点
       ↓
自己敲代码
       ↓
运行
       ↓
观察结果
       ↓
出现问题则 Debug
       ↓
完成独立练习
       ↓
更新 README / notes
       ↓
git commit
       ↓
git push
```

---

## 学习原则

1. 先预测程序输出，再运行验证。
2. 代码尽量自己手敲。
3. 遇到错误先阅读完整报错。
4. AI 优先提供解释和提示，不直接代替思考。
5. 每个知识点必须通过实际代码验证。
6. Python 学习不追求“大而全”，以硬件开发够用为标准。
7. 后期所有 Python 项目优先服务 STM32、传感器、测试和数据分析。
8. 每个学习日保留 GitHub 提交记录。

---

## 当前下一步

**Python Day 003：循环**

完成：

* [x] `sum_100.py`
* [x] `table99.py`
* [x] `countdown.py`

三道练习全部通过后，进入：

> **Python Day 004 — list 列表**

同时主要学习精力继续投入：

> **Embedded C + 电子硬件基础**
