class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
    def __init__(self):
    
    def heapify(self, lst):

    def heappush(self, val):
    
    def heappop(self):
    
    def __getitem__(self,i):
    
    def __len__(self):

'''
from typing import List

class Heap:
    def __init__(self, initial_lst=[]):
        self.heap = initial_lst
        if self.heap:
            self.heapify()
        self.heap_length = len(initial_lst) - 1

    def heapify(self):
        self.heap.sort()

    def insert(self, val):
        self.heap.append(val)
        self.heap_length += 1
        self.heapify_up(self.heap_length)
        #self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if self.heap_length == 0:
            return None
        if self.heap_length == 1:
            self.heap_length -= 1
            return self.heap.pop()
        
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heap_length -= 1
        self.heapify_down(0)
        return min_value

    def heapify_up(self, index:int) -> None:
        ''' Adjusts the order of the values in the heap, by undergoing binary heap.
        
        :type index: int
        '''
        parent_index = (index - 1) // 2
        while (index > 0 and 
               self.heap[index] < self.heap[parent_index]):
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def heapify_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        smallest = index

        if (left_index < self.heap_length and
            self.heap[left_index] < self.heap[smallest]):
            smallest = left_index
        
        if (right_index < self.heap_length and
            self.heap[right_index] < self.heap[smallest]):
            smallest = right_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)







class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_value

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        smallest = index

        if left_index < len(self.heap) and self.heap[left_index] < self.heap[smallest]:
            smallest = left_index

        if right_index < len(self.heap) and self.heap[right_index] < self.heap[smallest]:
            smallest = right_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

# Example usage:
heap = Heap([3, 5, 6, 8, 1])
print(heap.heap)
heap.insert(4)
heap.insert(7)
print(heap.heap)
heap.insert(2)
print(heap.heap)
heap.insert(9)
print(heap.heap)

print(heap.extract_min())  
print(heap.extract_min()) 
print(heap.heap)

# class Heap:
#     def __init__(self):
#         self.heap = None
#         self.heap_head = None

#     def heapify(self):

#     def heappush(self, val):
#         if not self.heap:
#             node = Node(val)
#             self.heap = node
#         else:
#             heap


#     def heappop(self):

#     def heapget(self):
#         return self.heap_head
    
#     def heaplength(self):
#         for 
    
