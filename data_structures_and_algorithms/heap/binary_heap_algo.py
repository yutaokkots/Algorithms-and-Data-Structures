'''
Binary Heap

'''

class HeapQueue:
    def __init__(self):
        self.heap = []

    def heappush(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heappop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_value = self.heap[0]
        # .pop() last element in heap, then assign to first element
        self.heap[0] = self.heap.pop()
        self.heap_down(0)
        return min_value

    def heapify_up(self, index):
        left_index = (index - 1) // 2
        while index > 0 and self.heap[left_index] > self.heap[index]:
            self.heap[left_index], self.heap[index] = self.heap[index], self.heap[left_index]
            index = left_index
            left_index = (index - 1) // 2

    def heap_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        smallest = index

        if left_index < len(self.heap) and self.heap[left_index] < self.heap[smallest]:
            smallest = left_index

        if right_index < len(self.heap) and self.heap[right_index] < self.heap[smallest]:
            smallest = right_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heap_down(smallest)



heap = HeapQueue()
heap.heappush(5)
print(heap.heap)

heap.heappush(4)
print(heap.heap)

heap.heappush(3)
print(heap.heap)

heap.heappush(2)
heap.heappush(1)
print(heap.heap)

popped_element_1 = heap.heappop()
popped_element_2 = heap.heappop()


print(popped_element_1, popped_element_2, heap.heap)
