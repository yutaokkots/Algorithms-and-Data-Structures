# in line swapping

x = 100
y = 50
print(f"x: {x}, y: {y}")
# x: 100, y: 50

#how do we swap the variables?

temp = y
y = x
x = temp

print(f"x: {x}, y: {y}")
# x: 50, y: 100

# how else to swap variable (one-line)
a = 1000
b = 20
print(f"a: {a}, b: {b}")

a, b = b, a         #### SWAP

print(f"a: {a}, b: {b}")

# a: 1000, b: 20
# a: 20, b: 1000
