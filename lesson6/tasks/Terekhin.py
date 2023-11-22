string = input()
for letter in string:
    if not (letter.isalpha() or letter.isspace()):
        string = string.replace(letter, '')
words_list = string.split()
for word in words_list:
    if len(word) >= 4:
        print(word)
