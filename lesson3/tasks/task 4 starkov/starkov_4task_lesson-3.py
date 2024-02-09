string = input().lower()

for letter_index in range(len(string) // 2):
    if string[letter_index] != string[-letter_index - 1]:
        print(False)
        break
else:
    print(True)
