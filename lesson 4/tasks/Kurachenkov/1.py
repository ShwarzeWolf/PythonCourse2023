import random

# Task 1
numbers = [random.randint(1, 100) for _ in range(100)]
sum_of_numbers = sum(numbers)
print("Sum of the numbers:", sum_of_numbers)