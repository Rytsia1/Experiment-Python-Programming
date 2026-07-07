numbers = []

print("Please enter 20 numbers:")
for i in range(20):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

lowest = min(numbers)
highest = max(numbers)
total = sum(numbers)
average = total / len(numbers)

print("\n--- Results ---")
print("Lowest number:", lowest)
print("Highest number:", highest)
print("Total of numbers:", total)
print("Average of numbers:", average)
