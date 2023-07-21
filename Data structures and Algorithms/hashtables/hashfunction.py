#hash
#a hash function maps strings to numbers. 
# i.e. hash maps, maps, dictionaries, associative arrays

# other examples:
# mapping a web address to an IP address -> process is called DNS resolution. 

#hash function tells you exactly where value is stored

#  ________ ________ ________ ________ ________
# |        |        |        |        |        | 
# |  1.49  |  0.79  |  2.49  |  0.67  |  1.49  | 
# |________|________|________|________|________|
#      0        1        2        3        4

# "apple" --> hash_function --> index 3 --> 0.67
# "milk"  --> hash_function --> index 0 --> 1.49

# hash function consistently maps a name to the same index
# hash function maps different strings to different indices
# hash function knows how big your array is and only returns valid indexes

# in python:
book = dict()
book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49
print(book)
# >>> {'apple': 0.67, 'milk': 1.49, 'avocado': 1.49}


## collisions -> for the following example hashmap, 'directory':
#  __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ 
# |__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|    
#  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18  ....
# 
# directory["apple"] = 0.67
# directory["banana"] = 0.39
#
#  "apple"
#  |  "banana"
#  |  |
#  __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __      __ 
# |a_|b_|c_|d_|e_|f_|__|__|__|__|__|__|__|__|__|__|__|__|__|    |z_|    
#  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18  ... 25
#
# but what if we want to include "avocado?" <- Causes collision with 'apple'
#
# Possible solution, use a linked list at the hash value
#
# ["apples"| 0.67 | ]--> ["avocados"| 1.49 | ]  LINKED LIST
#  |  ["banana"| 0.39 | ]
#  |  |
#  __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __      __ 
# |a_|b_|c_|d_|e_|f_|__|__|__|__|__|__|__|__|__|__|__|__|__|    |z_|    
#  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18  ... 25
#
# But having a long linked list will be problematic.
# IMPORTANT TO HAVE A VERY GOOD HASH FUNCTION

# HASH FUNCTION
#          average   worst case
#  ________ ________ ________ 
# |search  | O(1)   | O(N)   |
# |________|________|________|
# |insert  | O(1)   | O(N)   |
# |________|________|________|
# |delete  | O(1)   | O(N)   |
# |________|________|________|
#
#
# To avoid collisions, you need (1) a low load factor, (2) a good hash function
# Hash tables use an array for storage, 
# so you count the number of occupied slots in an array. 
# For example, this hash table has a load factor of 2/5, or 0.4.
#       __ __ __ __ __ 
#      |__|1_|__|0_|__|
#
# With a lower load factor, you’ll have fewer collisions, 
# and your table will perform better. A good rule of thumb is, 
# resize when your load factor is greater than 0.7.

# A good hash function distributes values in the array evenly.