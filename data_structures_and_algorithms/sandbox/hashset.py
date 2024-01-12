'''
hashset
Seen in LC0355 Design Twitter
Also see: "./defaultdict.py"
'''

from collections import defaultdict

hashset = defaultdict(set)

# hashset["a"]
# print(hashset)
# hashset["a"] = [1, 2, 1, 2, 1, 5, 4, 2]

print(hashset)

# hashset["a"] = 1
# hashset["a"] = 2
# hashset["a"] = 1
# hashset["a"] = 2
# hashset["a"] = 1
# hashset["a"] = 5
# hashset["a"] = 4
# hashset["a"] = 2
# print(hashset)

hashset["a"].add(1)
hashset["a"].add(2)
hashset["a"].add(1)
hashset["a"].add(2)
hashset["a"].add(1)
hashset["b"].add(5)
hashset["b"].add(4)
hashset["b"].add(2)
print(hashset)

if 2 in hashset["b"]:
    hashset["b"].remove(2)
print(hashset)