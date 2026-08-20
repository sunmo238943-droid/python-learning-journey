students = ["Tom", "Jack", "Lucy", "Mike"]

name = input("请输入名字：")

if name in students:
    print(f"找到 {name}")
    print(f"{name} 的下标是 {students.index(name)}")
else:
    print(f"没有找到 {name}")