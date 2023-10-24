digit_list = list(map(int, input('Массив чисел: ').split()))
check_list = []
for digit in digit_list:
    if digit in check_list:
        check_list.remove(digit)
    else:
        check_list.append(digit)
print(f'Число {check_list[0]} не повторяется')