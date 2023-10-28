'''
PEP 3132 - Extended Iterable Packing

This PEP proposes a change to iterable unpacking syntax, allowing to specify a “catch-all” name which will be assigned a list of all items not assigned to a “regular” name.


'''

a, *b, c = range(5)

print(a)
# 0
print(c)
# 4
print(*b)
# 1 2 3

seq = range(5)
first, rest = seq[0], seq[1:]
print(first, rest)
# 0 range(1, 5)

first, *rest = seq
print(first, rest)
# 0 [1, 2, 3, 4]

def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
        a, *res, b = res
    return res


