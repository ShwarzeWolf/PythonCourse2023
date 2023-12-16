#task 1
import random

numbers = [random.randint(1, 1000) for _ in range(100)]
print(numbers)

sum_numbers = sum(numbers)
print(sum_numbers)


#task 2
def find_number(numbers):
  for number in numbers:
    counter = 0
    for other_number in numbers:
      if number == other_number:
        counter += 1
    if counter == 1:
      return number
  return None

print("Введите массив чисел через пробел:")
numbers = list(map(int, input().split()))
odd_number = find_number(numbers)
print(odd_number)


#task 3
book = {
  "Иванов Иван Иванович": "+7 (912) 345-67-89",
  "Петров Петр Петрович": "+7 (922) 456-78-90",
  "Сидоров Сидор Сидорович": "+7 (932) 567-89-00",

}

for name, phone in book.items():
  print(f"Имя: {name}, телефон: {phone}")


#task  4
import turtle

turtle.shape('turtle')
turtle.speed(0)

radius = int(input("Введите радиус круга: "))
turtle.circle(radius)
#turtle.circle(25)

turtle.done()