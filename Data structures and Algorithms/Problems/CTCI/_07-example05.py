from typing import List
from random import randint
import heapq

# numbers are randomly generated and stored into an (expanding array)
# how would you keep track of the median?

class Solution():
    def __init__(self):
        self.random_list = []
        self.generate_rand_list()
        self.frequency_list = []
        self.maxheap = []
        self.create_maxheap()
        self.minheap = []
        self.create_minheap()
        
    def generate_rand_list(self):
        for _ in range(300): 
            number = randint(0, 10)
            self.random_list.append(number)

    def frequency(self):
        frequency_dict = {}
        for n in self.random_list:
            if n not in frequency_dict.keys():
                frequency_dict[n] = 1
            else:
                frequency_dict[n] += 1
        self.frequency_list = [[value, key] for key, value in frequency_dict.items()]

    def create_maxheap(self):
        self.frequency()
        negative_list = [[-num, key] for num, key in self.frequency_list]
        heapq.heapify(negative_list) 
        self.maxheap = negative_list

    def create_minheap(self):
        self.frequency()
        copy = self.frequency_list[:]
        heapq.heapify(copy)
        self.minheap = copy

    def get_median(self) -> int:
        return self.maxheap[0][1]

sol = Solution()
print(sol.random_list)
print(sol.maxheap)
print(sol.get_median())