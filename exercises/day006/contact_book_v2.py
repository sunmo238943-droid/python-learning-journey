def find_contact(book, name):
    if name in book:
        return book[name]
    else:
        return None
contacts = {
    "张三": "13800000001",
    "李四": "13800000002",
}
phone = find_contact(contacts, "张三")   # 存在的
print(phone)

phone = find_contact(contacts, "不存在的人")
if phone is None:
    print("查无此人")