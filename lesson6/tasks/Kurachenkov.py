import string

sentence = input("Введите строку: ")

sentence = sentence.translate(str.maketrans('', '', string.punctuation))

words = sentence.split()

for word in words:
    if len(word) < 4:
        print(word)
