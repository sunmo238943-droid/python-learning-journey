weight = float(input("体重(kg)："))
height = float(input("身高(m)："))

bmi = weight / height ** 2
print(f"你的BMI是：{bmi:.1f}")

if bmi < 18.5:
    print("偏瘦")
elif bmi < 24:
    print("正常")
elif bmi < 28:
    print("超重")
else:
    print("肥胖")