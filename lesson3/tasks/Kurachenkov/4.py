def is_palind(s):
    s = s.lower()
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

# Считываем строку от пользователя
inpu = input("Введите строку: ")

if is_palind(inpu):
    print("Это палиндром.")
else:
    print("Это не палиндром.")
