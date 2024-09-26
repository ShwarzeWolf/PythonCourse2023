import sys

a = 123_456

print(id(a))
print(type(a))
print(sys.getrefcount(a))

b = a
print(id(b))
print(type(b))
print(sys.getrefcount(b))
print(sys.getrefcount(a))

del a
print(sys.getrefcount(b))

###################### show in collab
a = 1000
b = 1000

print(a is b)

######################
l1 = [1, 2, 3, 4]
print(type(l1))
print(id(l1))
l2 = [1, 2, 3, 4]
print(id(l2))
print((l2 is l1))
print(l2 == l1)

# for i in l1:
#     print(id(i))
#     print(type(i))

l3 = l1
print(l3)

l3[0] = 1000
print(l1)

###############
c1 = ([1], 2, 3, 4)
c1[0].append(2)
print(c1)
# c1[0] = [1, 2]

try:
    c1[0] += [3]
except Exception as e:
    print(e)
    print('Exception occured')
    print(c1)