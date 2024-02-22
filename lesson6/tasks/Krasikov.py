inp = input()
for i in [", ", "; ", "  ", ",", ";"]:
    inp = inp.replace(i, " ")
a = [word for word in inp.split(" ") if len(word) < 4]
print(a)