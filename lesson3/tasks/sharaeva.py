# ### Задание 4
# Напишите программу, которая считывает строку и проверяет, является ли она палиндромом.
# Постарайтесь сделать ваш алгоритм оптимальным.
# "хакер в реках"

target_str = "хакер в реках".lower()

for letter_index in range(len(target_str) // 2):
    if target_str[letter_index] != target_str[-letter_index - 1]:
        print(False)
        break
else:
    print(True)
