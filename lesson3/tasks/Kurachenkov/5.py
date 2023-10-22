def is_correct(seq):
    stack = []

    for bracket in seq:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

print(is_correct('()'))
print(is_correct(')('))
print(is_correct('((()))'))
