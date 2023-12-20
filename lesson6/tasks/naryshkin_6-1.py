def find_short_words(string):
    words = string.replace(".", " ").replace(",", " ").replace(";", " ").replace("!", " ").replace("?", " ").split()
    for word in words:
        if len(word) < 4:
            print(word)


string = input("Введите строку: ")
find_short_words(string)