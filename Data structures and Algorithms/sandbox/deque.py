#Deque
# Double Ended Queue

#  Add Element at front                       Add Element at Rear
#    ______ ______ ______ ______ ______ ______ ______ 
#   |      |      |      |      |      |      |      |
#   |  10  |  15  |  20  |  30  |  40  |  55  |  60  |
#   |______|______|______|______|______|______|______|
#  
#  Remove element at front                    Remove Element at Rear

import collections

# main methods associated with deque:
# append(x)
# appendleft(x)
# pop()
# popleft()
# copy()                    create and return shallow copy
# extend(iterable)
# extendleft(iterable)      adds to left side in reverse
# rotate(y)                 rotate y places. -y is reverse
# clear()   
# count(x)                

q = collections.deque([1, 1, 1])
print(q)
# >>> deque([1, 1, 1])

q.appendleft(5)
print(q)
# >>> deque([5, 1, 1, 1])

q.append(12)
print(q)
# >>> deque([5, 1, 1, 1, 12])

left_pop = q.popleft()
print(left_pop)
# >>> 5

right_pop = q.pop()
print(right_pop)
# >>> 12

r = q.copy()
print(r)
# >>> deque([1, 1, 1])

q.extend([8, 7, 6])
print(q)
# >>> deque([1, 1, 1, 8, 7, 6])

q.extendleft([-3, -5, -2])
print(q)
# >>> deque([-2, -5, -3, 1, 1, 1, 8, 7, 6])         # reverses order

q.rotate(1)
print(q)
# >>> deque([6, -2, -5, -3, 1, 1, 1, 8, 7])

q.rotate(-2)
print(q)
# >>> deque([-5, -3, 1, 1, 1, 8, 7, 6, -2])

q.clear()
print(q)
# >>> deque([])

r_ct = r.count(1)
print(r_ct)
# >>> 3

# https://wiki.python.org/moin/TimeComplexity