punc_str = ",.\"\'/<>@!?#$;%^:?&*()[]{}`~|\\"
string = input("Enter the string:")
for i in string:
    if i in punc_str:
        string.replace(i, "")
string = string.split()
count = [j for j in string if len(j) < 4]
print(*count, sep=", ")
