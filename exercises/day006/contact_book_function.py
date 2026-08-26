def show_menu():
    print("=" * 30)
    print("       欢迎使用通讯录系统")
    print("=" * 30)
    print("1. 添加联系人")
    print("2. 删除联系人")
    print("3. 查询联系人")
    print("4. 显示所有联系人")
    print("0. 退出系统")
    print("=" * 30)

def find_contact(book, name):
    """查询联系人，存在返回电话号码，不存在返回None"""
    if name in book:
        return book[name]
    else:
        return None

def add_contact(book):
    """添加联系人"""
    name = input("请输入姓名：")
    if name in book:
        print(f"提示：{name} 已存在，电话号码为 {book[name]}")
    else:
        phone = input("请输入电话号码：")
        book[name] = phone
        print(f"✅ 成功添加：{name} -> {phone}")

def delete_contact(book):
    """删除联系人"""
    name = input("请输入要删除的姓名：")
    if name in book:
        del book[name]
        print(f"✅ 已删除 {name}")
    else:
        print(f"❌ 提示：{name} 不存在")

def query_contact(book):
    """查询联系人（使用重构后的函数）"""
    name = input("请输入姓名：")
    phone = find_contact(book, name)  # 调用函数查询
    if phone is None:
        print(f"❌ 提示：{name} 不存在")
    else:
        print(f"✅ 查询结果：{name} -> {phone}")

def show_all(book):
    """显示所有联系人"""
    if not book:
        print("📭 通讯录为空")
    else:
        print("\n--- 所有联系人 ---")
        for name, phone in book.items():
            print(f"  {name} -> {phone}")
        print(f"共 {len(book)} 个联系人\n")

def main():
    """主程序"""
    address_book = {}
    
    while True:
        show_menu()
        choice = input("请选择操作（0-4）：")
        
        if choice == "1":
            add_contact(address_book)
        elif choice == "2":
            delete_contact(address_book)
        elif choice == "3":
            query_contact(address_book)
        elif choice == "4":
            show_all(address_book)
        elif choice == "0":
            print("👋 感谢使用，再见！")
            break
        else:
            print("❌ 无效输入，请重新选择")
        print()

# 程序入口
main()