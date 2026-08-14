weight = float(input("请输入体重（kg）："))
height = float(input("请输入身高（m）："))

bmi = weight / (height ** 2)

print(f"你的BMI为：{bmi:.2f}")