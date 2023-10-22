from random import randint

digit_list = [randint(0, 100) for i in range(100)]
print(sum(digit_list))