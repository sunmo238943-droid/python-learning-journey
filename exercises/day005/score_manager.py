scores = []

for i in range(5):
    score = int(input(f"请输入第 {i + 1} 个成绩："))
    scores.append(score)

print("所有成绩：", scores)

print("最高分：", max(scores))
print("最低分：", min(scores))
print("总分：", sum(scores))
print(f"平均分：{sum(scores) / len(scores):.2f}")

ascending = sorted(scores)
descending = sorted(scores, reverse=True)

print("从低到高：", ascending)
print("从高到低：", descending)
print("原始成绩：", scores)

search_score = int(input("请输入要查询的成绩："))

if search_score in scores:
    print("找到了这个成绩")
else:
    print("没有这个成绩")