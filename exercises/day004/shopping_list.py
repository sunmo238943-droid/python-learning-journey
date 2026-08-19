shopping_list=["milk","bread","egg"]
print("start:",shopping_list)
shopping_list.append("apple")
shopping_list.remove("bread")
print("final:",shopping_list)
print(len(shopping_list))
print()
for item in shopping_list:
 print(item)