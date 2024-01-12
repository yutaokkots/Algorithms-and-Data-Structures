import heapq
# documentation: https://docs.python.org/3/library/heapq.html

li = [1, 5, 1, 1, 2, 3, 4, 4, 5, 6]
print(li)
# [1, 5, 1, 1, 2, 3, 4, 4, 5, 6]

#made into heap, printed items are different. 
heapq.heapify(li)

print(li)
# [1, 1, 1, 4, 2, 3, 4, 5, 5, 6]
#       
#                1
#              /   \
#             1      1
#           /  \    /  \
#         4     2  3    4
#        / \   / 
#       5   5 6      

# Other heapq commands
# heappush(heapname, item)  # add an item to the heap
# heappop(heapname)         # take out the smallest item from the heap

heapq.heappush(li, 12)
print(li)
# [1, 1, 1, 4, 2, 3, 4, 5, 5, 6, 12]
#                1
#              /   \
#             1      1
#           /  \    /  \
#         4     2  3    4
#        / \   / \
#       5   5 6   12   

first_pop = heapq.heappop(li)
print(first_pop)
print(li)
# 1
# [1, 1, 3, 4, 2, 12, 4, 5, 5, 6]
#
#                1
#              /   \
#             1      3
#           /  \    /  \
#         4     2  12    4
#        / \   / 
#       5   5 6      
#
##########################
##### how to get max-heap?
# negate the numbers when putting in, negate numbers when popping out. 


#############################################
########         Min Heap            ########
#############################################
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def heapify(self, lst):
        heapq.heapify(lst)
        self.heap = lst

    def heappush(self, val):
        heapq.heappush(self.heap, val)
    
    def heappop(self):
        return heapq.heappop(self.heap)
    
    def __getitem__(self,i):
        return self.heap[i]
    
    def __len__(self):
        return len(self.heap)


# examples
new_list = [21, 5, 3, 23, 59, 11, 89, 191]
new_list_2 = [21, 5, 3, 23, 59, 11, 89, 191, 135, 240]

# instantiate MinHeap class
minHeap = MinHeap()
print(minHeap.heap)
# print() -> []

minHeap.heapify(new_list)
print(minHeap.heap)
# print() -> [3, 5, 11, 23, 59, 21, 89, 191]
#
#                3
#              /   \
#             5      11
#           /  \    /  \
#         23   59  21   89
#        / 
#       191
#
minHeap.heappush(145)
print(minHeap.heap)

#############################################
########         Max Heap            ########
#############################################

class MaxHeap():
    def __init__(self):
        self.heap = []
    
    def heappush(self, val):
        heapq.heappush(self.heap, -val)

    def heappop(self):
        value = heapq.heappop(self.heap)
        return -value

    def heapify(self, lst):
        lst = [-n for n in lst]
        heapq.heapify(lst)    
        self.heap = lst

# instantiate maxHeap clas
maxHeap = MaxHeap()

# print out maxHeap.heap before heapifying
print(maxHeap.heap)
# print() -> []

# print out maxHeap.heap after heapifying
maxHeap.heapify(new_list_2)
print(maxHeap.heap)
#print() -> [-240, -191, -89, -135, -59, -11, -3, -23, -21, -5]
#
#                  -248
#                 /     \
#             -191      -89
#            /  \       /   \
#        -135    -59   -11  -3
#        /   \    /
#      -23  -21  -5
#
max_value = maxHeap.heappop()
print(max_value)
# print() -> 240 (the maxHeap class multiples the popped number with (-1))
print(maxHeap.heap)
# print() -> [-191, -135, -89, -23, -59, -11, -3, -5, -21]
#                  -191
#                 /     \
#             -135      -89
#            /  \       /   \
#        -23     -59   -11   -3
#        /   \   
#      -5  - 21  