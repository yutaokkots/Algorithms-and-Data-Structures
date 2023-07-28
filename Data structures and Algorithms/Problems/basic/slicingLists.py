## How do you 'splice' in python?
# splicing does not exist, but with slicing, you can achieve:
# 1) Slicing
# 2) Replacing
# 3) Inserting
# 4) Removing

the_list:any = [0, 1, 2, 3, "d", 5, 6, "e"]

##############
# 1) Slicing
print(the_list[4:8])
# ['d', 5, 6, 'e']

# ** slicing does not affect the original list
print(the_list)
# [0, 1, 2, 3, 'd', 5, 6, 'e']

##############
# 2) Replacing
the_list[5:7] = ["u", "n"]

print(the_list)
# [0, 1, 2, 3, 'd', 'u', 'n', 'e']

##############
# 3) Inserting
the_list[4:4] = ["s","a","n","d"]

print(the_list)
# [0, 1, 2, 3, 's', 'a', 'n', 'd', 'd', 'u', 'n', 'e']

##############
# 4) Removing
the_list[0:4] = []

print(the_list)
# ['s', 'a', 'n', 'd', 'd', 'u', 'n', 'e']

##############
# 5) Inserting again (at the end)
length = len(the_list)
the_list[length:length] = ["national park"]

print(the_list)