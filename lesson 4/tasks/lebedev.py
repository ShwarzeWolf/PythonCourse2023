import random
import turtle
from typing import Any

# TASK 1
# Создайте список из 100 рандомных чисел. Посчитайте сумму этих чисел
numbers = []

for i in range(100):
    num = random.randint(1, 1000)
    numbers.append(num)

print("task 1")
print(sum(numbers))
print("")

# TASK 2
# Дан массив чисел, каждое из которых повторяется 2 раза, кроме одного. 
# Найдите это непарное число.
def find_num(lst):
    max_num = max(lst)
    perfect_list = [i for i in range(1, max_num + 1)] * 2

    current_sum = sum(lst)
    expected_sum = sum(perfect_list)

    return expected_sum - current_sum


list_A = [1, 1, 2, 3, 3, 4, 4]
list_B = [1, 2, 3, 4, 5, 1, 2, 3, 5]

print("task 2")
print(find_num(list_A))
print(find_num(list_B))
print("")


# TASK 3
# Создайте словарь-аналог телефонной книги. Занесите туда 3 записи. 
# Выведите все записи в консоль
class Person:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age
        (self.first_name, self.second_name, self.last_name) = self.split_full_name()
    
    def split_full_name(self):
        name_parts = self.full_name.split()

        first_name = name_parts[0] if len(name_parts) > 0 else None
        second_name = name_parts[1] if len(name_parts) > 1 else None
        last_name = name_parts[2] if len(name_parts) > 2 else None
        
        return first_name, second_name, last_name
    
    def __repr__(self):
        return f"Person({self.full_name}, {self.age})"


def count_indents(_list: list):
    '''
    Counts the number of whitespace characters needed to make a list look like table rows

    :param _list: a list of strings to count indents
    :returns: lust of numbers of whitespace characters for each column
    '''
    longest_word = max(_list, key=len)
    biggest_length = len(longest_word)

    indents = list()

    for current_word in _list:
        length = len(current_word)
        indents.append(biggest_length - length + 1)

    return indents


phone_book = {}
phone_book["+"] = Person("Alexander Sergeevich Pushkin", 224)
phone_book["+7 (999) 999-99-99"] = Person("Tom Smith", 1)
phone_book["+1 (911) 577-91-40"] = Person("Moshennik", 39)


print("task 3")

phones = phone_book.keys()
indents = count_indents(phones)

iteration = 0
for phone, person in phone_book.items():
    print(f"Phone: {phone} {indents[iteration] * ' '} Person: {person.__repr__()}")
    iteration += 1
print()


# TASK 4
turtle.circle(100)
turtle.exitonclick()
