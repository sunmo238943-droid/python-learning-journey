scores = [78, 92, 65, 88, 96, 81]

print("原始成绩：", scores)

print("最高分：", max(scores))
print("最低分：", min(scores))
print("总分：", sum(scores))
print(f"平均分: {sum(scores) / len(scores):.2f}")

scores.sort()

print("从低到高：", scores)

scores.sort(reverse=True)

print("从高到低：", scores)