a=input()
a1=a[::-1]
c=0
b=a.count("(")
b1=a.count(")")
for i in range(len(a)):
    if a[i]==a1[i]:
        c+=1
if c==0 and b==b1:
    print("Эта строка - правильная")
else:
    print("Эта строка - неправильная")