# TASK 1
def squares_sum(*nums):
    return sum(num ** 2 for num in nums)


# TASK 2
def assert_numbers(*nums):
    numbers_flags = [isinstance(num, (int, float)) for num in nums]

    if not all(numbers_flags):
        print("ERROR: Non-number element detected")
    
    return None


# TASK 3
def multiple_upper(*strings):
    upper_strings = list(map(lambda x: x.upper(), strings))
    return upper_strings


# TASK 4
def factorial(n):
    if n < 1:
        return 1
    
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(squares_sum(1, 5, 6, 2, 10))

    print(1, assert_numbers(1, 5, 6, 2, 10))
    print(2, assert_numbers(1, 5, 6, 2, "10"))

    print(multiple_upper("string12", "StrInG10    /*", "STRIIINIGNN"))
    
    print(factorial(10))