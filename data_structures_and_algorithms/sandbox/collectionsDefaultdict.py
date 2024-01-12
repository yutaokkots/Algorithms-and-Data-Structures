import collections

# way to create a graph?
# what is the difference between collections.defaultdict and normal dictionary?

# d.get(key, default) won't ever modify your dictionary – it will just return the default and leave the dictionary unchanged. 
# defaultdict, on the other hand, will insert a key into the dictionary if it isn't there yet.

# A defaultdict works exactly like a normal dict, but it is initialized with a function (“default factory”) 
# # that takes no arguments and provides the default value for a nonexistent key.

# A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.
################################
## collections.defaultdict(default_factory=None, /[, ...])

####### ####### #######
## default_factory = list
##
## the difference between a collections.defaultdict and {} to initialize a dictionary is:
## an instantiated collections.defaultdict() allows adding a value to a key if the key doesn't exist

d_list = collections.defaultdict(list)

s = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]

for k, v in s:
    d_list[k].append(v)

print(d_list)

# >>> 
# defaultdict(<class 'list'>, 
#  {
#       'yellow': [1, 3], 
#       'blue': [2, 4], 
#       'red': [1]
# })

####### ####### #######
## regular dictionary, using Dict.setDefault()

s = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]

dict_normal = {}

for k, v in s:
    dict_normal.setdefault(k, []).append(v)

print(dict_normal)

# >>> {
#   'yellow': [1, 3], 
#   'blue': [2, 4], 
#   'red': [1]
#   }

####### ####### #######
## useful for counting
## default_factory = int

d_int = collections.defaultdict(int)

s = "mississippi"

for k in s:
    d_int[k] += 1

print(d_int)

# >>> 
# defaultdict(<class 'int'>, 
#  {
#       'm': 1, 
#       'i': 4, 
#       's': 4, 
#       'p': 2
# })


####### ####### #######
## build a dictionary of sets
## default_factory = set

d_set = collections.defaultdict(set)

s = [('red', 1), ('red', 1), ('red', 1), ('red', 2), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]

for k, v in s:
    d_set[k].add(v)

print(d_set)

# >>> 
# defaultdict(<class 'set'>, 
# {
#       'red': {1, 2, 3}, 
#       'blue': {2, 4}
# })

####### ####### #######
## default_factory = dict

d_set = collections.defaultdict(dict)