import random

secret = random.randint(1, 100)
count = 0

while True:
    guess = int(input("请输入你猜的数字："))
    count += 1

    if guess > secret:
        print("big")

    elif guess < secret:
        print("smaller")

    else:
        print (f"right!sum{count}")
        break        # 跳出循环