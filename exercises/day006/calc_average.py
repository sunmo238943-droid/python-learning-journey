def calc_average(scores):
    total = sum(scores)
    return total / len(scores)
result = calc_average([90, 80, 70])
print(result)