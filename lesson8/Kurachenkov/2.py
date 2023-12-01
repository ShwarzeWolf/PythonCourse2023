def sum_of_squares(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            print("Error: All arguments must be numbers.")
            return None
    return sum(arg**2 for arg in args)