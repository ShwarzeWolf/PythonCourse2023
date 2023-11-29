strings = ["привет", "мир", "собака"]

upped_text = lambda s: s.upper()

upper_strings = list(map(upped_text, strings))
print(upper_strings)
