numbers = [30, 40, 50, 60, 70]
print(f"List: {numbers}\n")


built_in_sum = sum(numbers)
print("--- Method 1 (Built-in) ---")
print(f"Total = {built_in_sum}\n")


total = 0
for num in numbers:
    total += num  

print("--- Method 2 (Manual Loop) ---")
print(f"Total = {total}")
