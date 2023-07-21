import heapq

li = [5, 7, 9, 1, 3]
minus_li = [-s for s in li]
heapq.heapify(minus_li)
heapq.heapify(li)
print(minus_li)
print(li)
print(type(li))

li2 = [2,7,4,1,8,1]
heapq.heapify(li2)
print(li2)
# >>> [1, 1, 2, 7, 8, 4]
#            1
#           /  \
#         1      2
#        / \    / 
#       7   8  4
#

### 

# def heapify(list, N, i):
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
#     if left < N and list[left] > list[largest]:
#         largest = left
#     if right < N and list[right] > list[largest]:
#         largest = right
#     if largest != i:
#         list[i], list[largest] = list[largest], list[i]
#         heapify(list, N, largest)

# print(heapify(li2, len(li2), 2))


class Heap_algo:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return (i - 1) // 2

### heap algorithm 


class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.heapify_up(self.size - 1)

    def extract_min(self):
        if self.size == 0:
            return None

        min_item = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        del self.heap[self.size - 1]
        self.size -= 1
        self.heapify_down(0)

        return min_item

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.heapify_down(smallest)

heap = Heap()
for item in li2:
    heap.insert(item)


    # def parent(self, i):
    #     return (i - 1) // 2

    # def insert(self, item):
    #     self.heap.append(item)
    #     self.size += 1
    #     self.heapify_up(self.size - 1)

    # def heapify_up(self, i):
    #     while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
    #         self.swap(i, self.parent(i))
    #         i = self.parent(i)

    # def swap(self, i, j):
    #     self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

sorted_items = []
while heap.size > 0:
    sorted_items.append(heap.extract_min())

print(sorted_items)

print(sorted_items)
for item in sorted_items:
    print(heap.left_child(item))
    print(heap.right_child(item))