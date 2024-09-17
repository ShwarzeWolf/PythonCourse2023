def sum_of_squares(*args):
  for arg in args:
    if not isinstance(arg, (int, float)):
      print("Неверный тип аргумента:", arg)
      return None
  return sum(arg ** 2 for arg in args)

print(sum_of_squares(2, 5, 'sobaka'))