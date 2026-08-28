import calc_tools

temperatures = [23.5, 26.8, 19.2, 31.5, 22.0]

avg = calc_tools.calculate_average(temperatures)
max_val = calc_tools.find_max(temperatures)

print(f"Average: {avg}")
print(f"Max: {max_val}")