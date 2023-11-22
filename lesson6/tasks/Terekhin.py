string = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for letter in string:
    if letter.lower() not in alphabet:
        string = string.replace(letter, '')
words_list = string.split()
for word in words_list:
    if len(word) >= 4:
        print(word)
