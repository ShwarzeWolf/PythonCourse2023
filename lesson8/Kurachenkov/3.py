strings = ["hello", "world", "привет"]
uppercase_lambda = lambda s: s.upper()
uppercase_strings = list(map(uppercase_lambda, strings))
