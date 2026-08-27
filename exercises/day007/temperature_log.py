#!/usr/bin/env python3
"""
exercises/day007/temperature_log.py
温度日志读写演示程序
"""

# 测试数据：5 个温度值
temperatures = [23.5, 26.8, 19.2, 31.5, 22.0]

# ============ 第一步：写入文件 ============
# 使用 "w" 模式写入，会覆盖已有文件
with open("temperature.txt", "w") as file:
    for temp in temperatures:
        file.write(f"{temp}\n")  # 每个温度占一行
print("✓ 已写入 5 个温度到 temperature.txt")

# ============ 第二步：读取文件 ============
# 使用 "r" 模式读取刚才写入的内容
print("\n--- 读取文件内容 ---")
with open("temperature.txt", "r") as file:
    lines = file.readlines()  # 读取所有行
    for line in lines:
        print(f"  温度: {line.strip()}")  # strip() 去掉换行符

# ============ 第三步：验证追加模式 ============
# 使用 "a" 模式追加新数据，验证不会覆盖原有内容
print("\n--- 追加新数据 ---")
extra_temps = [18.5, 27.3]
with open("temperature.txt", "a") as file:
    for temp in extra_temps:
        file.write(f"{temp}\n")
print(f"✓ 已追加 {len(extra_temps)} 个温度")

# 读取完整文件，验证追加成功
print("\n--- 追加后的完整文件 ---")
with open("temperature.txt", "r") as file:
    all_lines = file.readlines()
    for i, line in enumerate(all_lines, 1):
        print(f"  第{i}行: {line.strip()}")

# ============ 第四步：温度数据分析（进阶功能） ============
print("\n--- 温度数据分析 ---")

# 从文件读取温度并转换为 float 列表
temperatures_from_file = []
with open("temperature.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:  # 跳过空行
            temperatures_from_file.append(float(line))

# 计算平均值和最大值
if temperatures_from_file:
    avg_temp = sum(temperatures_from_file) / len(temperatures_from_file)
    max_temp = max(temperatures_from_file)
    
    print(f"总温度数: {len(temperatures_from_file)}")
    print(f"平均温度: {avg_temp:.2f}°C")
    print(f"最高温度: {max_temp:.1f}°C")
else:
    print("文件为空，无数据可分析")