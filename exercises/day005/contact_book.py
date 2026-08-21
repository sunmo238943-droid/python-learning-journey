# Python Day 004 练习
address_book = {}

def show_menu():
    print("\n=== 通讯录 ===")
    print("1. 添加联系人")
    print("2. 删除联系人")
    print("3. 查询联系人")
    print("0. 退出")

while True:
    show_menu()
    choice = input("请选择操作: ")
    
    if choice == "1":
        name = input("请输入姓名: ")
        phone = input("请输入电话: ")
        address_book[name] = phone
        print(f"已添加：{name} -> {phone}")
    
    elif choice == "2":
        name = input("请输入姓名: ")
        if name in address_book:
            del address_book[name]
            print(f"已删除：{name}")
        else:
            print(f"提示：{name} 不存在")
    
    elif choice == "3":
        name = input("请输入姓名: ")
        if name in address_book:
            print(f"查询结果：{name} -> {address_book[name]}")
        else:
            print(f"提示：{name} 不存在")
    
    elif choice == "0":
        print("已退出，再见！")
        break
    
    else:
        print("无效选项，请重新输入")



