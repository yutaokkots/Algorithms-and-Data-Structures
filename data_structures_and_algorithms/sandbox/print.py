# in python, the print statement has a few more parameters
# print(*object)
# print(*object, sep="-")
# print(*object, sep="-", end="stop")

# instead of printing each item in the iterable in a for loop,
iterable = [11, 5, 42, 15, 122, 66, 1, 32, 34, 10, 90, 201]

print(iterable)
# >>> [11, 5, 42, 15, 122, 66, 1, 32, 34, 10, 90, 201]

for n in iterable:
    print(n)
# 11
# 5
# 42
# 15
# 122
# 66
# 1
# 32
# 34
# 10
# 90
# 201

#do this instead:
print(*iterable)
# >>> 11 5 42 15 122 66 1 32 34 10 90 201

##### ALSO declare a SEPARATOR

print(*iterable, sep=" --> ")
# 11 --> 5 --> 42 --> 15 --> 122 --> 66 --> 1 --> 32 --> 34 --> 10 --> 90 --> 201


print(*iterable, sep=" --> ", end=" WHOA!")
# 11 --> 5 --> 42 --> 15 --> 122 --> 66 --> 1 --> 32 --> 34 --> 10 --> 90 --> 201 WHOA!