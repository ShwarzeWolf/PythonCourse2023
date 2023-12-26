sequence = input()

depth = 0
''' Checks current depth of brackets sequence '''
for symbol in sequence:
    if symbol == "(":
        depth += 1
    elif symbol == ")":
        depth -= 1
    
    if depth < 0:
        # We've got unpaired closing bracket
        print(False)
        break
else:
    print(depth == 0)
