##########################
##  and, logical truth using sets
##########

lst1 = ["hello", "cup", "simple", "banana", "water", "clock"]
lst2 = ["hello", "water", "fire", "apple", "cup", "air"]
lst3 = ["ni hao", "water", "air", "banana", "bowl", "simple"]

set_1 = set(lst1)
set_2 = set(lst2)
set_3 = set(lst3)

######################
##  combination 1 + 2
combo_1_2 = (set_1 & set_2)
print(combo_1_2)
# {'cup', 'hello', 'water'}

######################
##  combination 2 + 3
combo_2_3 = (set_2 & set_3)
print(combo_2_3)
# {'air', 'water'}

######################
##  combination 1 + 3
combo_1_3 = (set_1 & set_3)
print(combo_1_3)
# {'water', 'simple', 'banana'}

######################
##  combination 1 + 2 + 3
combo_1_2_3 = (set_1 & set_2 & set_3 )
print(combo_1_2_3)
# {'water'}

######################
##  subtract sets -> (combo 1 + 2) - set_3
print(combo_1_2 - set_3)
# {'cup', 'hello', 'water'} - {'banana', 'air', 'ni hao', 'simple', 'water', 'bowl'}

# {'hello', 'cup'}

######################
##  subtract sets -> set_3 - (combo 1 + 2) 
print(set_3 - combo_1_2)
# {'banana', 'air', 'ni hao', 'simple', 'water', 'bowl'} - {'cup', 'hello', 'water'} 

# {'ni hao', 'simple', 'air', 'bowl', 'banana'}