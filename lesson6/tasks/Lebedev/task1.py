import re

string = input("enter a string to find words that have less than 4 characters: ")
normalized_string = re.sub(r"[^a-zа-яё\s]", "", string, flags = re.IGNORECASE)

words = normalized_string.split()

long_words = [word for word in words if len(word) < 4]

print("\n".join(long_words))
