def greet(name,greeting="Hello"):
    print(f"{greeting},{name}!")

greet("San Zhang")
greet("Si li","Good morning")



def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(lo, hi)              # 预测：？