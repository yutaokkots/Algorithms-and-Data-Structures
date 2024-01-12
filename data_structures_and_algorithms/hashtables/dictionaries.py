# Dictionaries in python
# all of the following create the same dictionary:
# d = {
#   "one":1
#   "two":2
#   "three":3
# }

# doesn't require declaring the keys as strings
a = dict(one=1, two=2, three=3)

# most common way to create dictionary, and comparable to objects in javascript
b = {'one': 1, 'two': 2, 'three': 3}

# zipping two lists together
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

# creating a dictionary from a sset of tuples
d = dict([('two', 2), ('one', 1), ('three', 3)])

# using dict() to create a dictionary {}
e = dict({'three': 3, 'one': 1, 'two': 2})

# mixing up different formats 
f = dict({'one': 1, 'three': 3}, two=2)

# >>> print(a == b == c == d == e == f)
# >>> True


#################################
##### SORTING DICTIONARIES  #####
#################################

# sorted()

## BEFORE Python 3.6, Dictionaries were inherently unsorted. 
## Dictionaries were implementations of hashmaps. 
## FROM Python 3.7, sorting of dictionaries is guaranteed. 

members = ["Jim", "Jack", "Jane", "Jill", "Joe", "Jess"]
experience = [2, 3, 1, 5, 4, 1]

#############
# create a dictionary by zipping two lists together
people = dict(zip(members, experience))
print(people)
#  original   >>>  {'Jim': 2, 'Jack': 3, 'Jane': 1, 'Jill': 5, 'Joe': 4, 'Jess': 1}

#############
# Sort by key
sorted_people_key = dict(sorted(people.items()))
print(sorted_people_key)
#  key        >>>  {'Jack': 3, 'Jane': 1, 'Jess': 1, 'Jill': 5, 'Jim': 2, 'Joe': 4}

#############
# Sort by Value
sorted_people_value = dict(sorted(people.items(), key=lambda item:item[1]))
print(sorted_people_value)
#  value      >>>  {'Jane': 1, 'Jess': 1, 'Jim': 2, 'Jack': 3, 'Joe': 4, 'Jill': 5}

#############
# Sort by value reversed
sorted_people_value_rev = dict(sorted(people.items(), reverse=True, key=lambda item:item[1]))
print(sorted_people_value_rev)
#  value rev  >>>  {'Jill': 5, 'Joe': 4, 'Jack': 3, 'Jim': 2, 'Jane': 1, 'Jess': 1}

# together:
# {'Jim': 2, 'Jack': 3, 'Jane': 1, 'Jill': 5, 'Joe': 4, 'Jess': 1}
# {'Jack': 3, 'Jane': 1, 'Jess': 1, 'Jill': 5, 'Jim': 2, 'Joe': 4}
# {'Jane': 1, 'Jess': 1, 'Jim': 2, 'Jack': 3, 'Joe': 4, 'Jill': 5}
# {'Jill': 5, 'Joe': 4, 'Jack': 3, 'Jim': 2, 'Jane': 1, 'Jess': 1}

##########################
## LAMBDA function in sorted()
## Why does the 'key=lambda item:item[1]' sort via values?
## essentially, 'key=lambda item:item[1]' is an inline function

# key=lambda item:item[1] is equal to:
# lambda arguments: expression

def sorter(item):
    return item[1]

roman_nums = {'I':1, 
              'II':2, 
              'III':3, 
              'IV':4, 
              'V':5, 
              'VI':6,
              'VII':7,
              'VIII':8,
              'IX':9,
              'X':10}

rev_sorted_roman = dict(sorted(roman_nums.items(), reverse=True, key=lambda x: sorter(x)))
print(rev_sorted_roman)
#  >>>  rev_sorted_roman = {
#  >>>      'X': 10, 
#  >>>      'IX': 9, 
#  >>>      'VIII': 8, 
#  >>>      'VII': 7, 
#  >>>      'VI': 6, 
#  >>>      'V': 5, 
#  >>>      'IV': 4, 
#  >>>      'III': 3, 
#  >>>      'II': 2, 
#  >>>      'I': 1
#  >>>      }

##########################
## What does the 'item[1]', and particularly, '[1]' do in 'key=lambda item:item[1]'?
##
# the [1] indicates that index=1 in the tuple, in this case, the 'value' in the '(key, value)' tuple
# is used to sort. 

# for instance: given an array of tuples
club_info = [("dave", 19, 9673),
("jess", 48, 3261),
("jenny", 23, 5899),
("oscar", 78, 7801),
("sally", 27, 2231)]

sorted_name = sorted(club_info, 
                     key=lambda x:x[0])

sorted_age_rev = sorted(club_info, 
                        reverse=True, 
                        key=lambda x:x[1])

sorted_number = sorted(club_info, 
                       key=lambda x:x[2])

print(sorted_name)   
print(sorted_age_rev) 
print(sorted_number)  
# sorted_name    = [('dave', 19, 9673), ('jenny', 23, 5899), ('jess', 48, 3261), ('oscar', 78, 7801), ('sally', 27, 2231)]
# sorted_age_rev = [('oscar', 78, 7801), ('jess', 48, 3261), ('sally', 27, 2231), ('jenny', 23, 5899), ('dave', 19, 9673)]
# sorted_number  = [('sally', 27, 2231), ('jess', 48, 3261), ('jenny', 23, 5899), ('oscar', 78, 7801), ('dave', 19, 9673)]