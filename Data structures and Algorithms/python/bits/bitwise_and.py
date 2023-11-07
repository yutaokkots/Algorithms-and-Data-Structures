'''
& -> Bit operator


'''
##########################
##  and, logical truth
##########
a = 14
b = 4

print(b and a)
# >>> 14

# 1) evaluates b (b = 4), therefore is true
# 2) moves to second variable
# 3) evalutes a (a = 14), therefore is true
# 4) outputs value of b, 14

##########################
##  bitwise & operation
##########

print(a & b)
# >>> 4

# 1) evaluates b (b = 4), as    0000 0100
# 2) evaluates a (a = 14), as   0000 1110
#    what is evaluated:               ^   bit of 4 and 10 are '1' at this position 
# 3) outputs a & b as           0000 0100

#####################
##  example

c, d = 9, 10

print(c and d)

# 1) evaluates c (c = 9; not 0 or False), therefore is true
# 2) moves to second variable
# 3) evalutes d (d = 10; not 0 or False), therefore is true
# 4) outputs value of d, 10, because it was evaluated last

# >>> 10

print(c & d)

# 1) evaluates c (c = 9), as    0000 1001
# 2) evaluates d (d = 10), as   0000 1010
#    what is evaluated:              ^    bit of 9 and 10 are '1' at this position 
# 3) outputs c & d as           0000 1000

# >>> 8


print("######## ---- ####### \n")

lst1 = ["hello", "battery", "headphone", "toilet paper", "sticker"]
lst2 = ["hat","toilet paper","captain","wrench","battery"]
lst3 = ["boat", "toilet paper", "ninja", "smoke"]

set_1 = set(lst1)
set_2 = set(lst2)
set_3 = set(lst3)

print(set_1 & set_2)
# {'toilet paper', 'battery'}

print(set_1 - set_2)
# {'hello', 'sticker', 'headphone'}

print(set_2 - set_1)
# {'captain', 'wrench', 'hat'}

print(set_1 & set_2 & set_3)
# {'toilet paper'}