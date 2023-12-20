def some_func(a, b, *args, **kwargs):
   print(args)
   print(kwargs)

some_func(1, 2, 3, 4, f=6)