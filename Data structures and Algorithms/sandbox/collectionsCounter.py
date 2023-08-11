import collections

# https://docs.python.org/3/library/collections.html#collections.Counter

# A counter is a dict subclass for counting hashable objects. 

nums = [1, 2, 1, 2, 3, 2, 3, 5, 2, 12, 1, 1, 13, 12, 23, 98, 3, 3, 3, 4, 5, 23]

c = collections.Counter(nums)

print(c)
# Counter({
#   3: 5, 
#   1: 4, 
#   2: 4, 
#   5: 2, 
#   12: 2, 
#   23: 2, 
#   13: 1, 
#   98: 1, 
#   4: 1})

print(c[3])
# >>> 5
print(c[2])
# >>> 4