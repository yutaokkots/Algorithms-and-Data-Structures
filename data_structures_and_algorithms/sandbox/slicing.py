# Slicing notes

# get all of the elements except the last one

iterable = [11, 5, 42, 15, 122, 66, 1, 32, 34, 10, 90, 201]

copy = iterable[:-1]
print(copy)
# copy = [11, 5, 42, 15, 122, 66, 1, 32, 34, 10, 90]


# REVERSE
copy2 = iterable[::-1]
print(copy2)
# copy2 = [201, 90, 10, 34, 32, 1, 66, 122, 15, 42, 5, 11]