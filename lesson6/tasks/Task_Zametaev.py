a = input()
lst = a.split(" ")
znaki = [".", "?", "!", "...", ":", ".,", ",", "-", "--", "(", ")"]
for i in lst:
    counter = 0
    for g in i:
        if g not in znaki:
            counter += 1
    if counter == 4:
        print(i)