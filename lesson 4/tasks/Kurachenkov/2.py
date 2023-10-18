# Task 2
def find_unpaired_number(numbers):
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for num, count in count_dict.items():
        if count == 1:
            return num


numbers = [1, 1, 2, 3, 3, 4, 4]
unpaired_number = find_unpaired_number(numbers)
print(unpaired_number)