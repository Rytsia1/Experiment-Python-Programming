import random

random_list = [random.randint(0, 100) for _ in range(28)]
print("Original list:")
print(random_list)

odd_index_values = [random_list[i] for i in range(1, len(random_list), 2)]
odd_index_values.sort()

for i, val in enumerate(odd_index_values):
    random_list[1 + i*2] = val

print("\nModified list (odd indices sorted):")
print(random_list)
