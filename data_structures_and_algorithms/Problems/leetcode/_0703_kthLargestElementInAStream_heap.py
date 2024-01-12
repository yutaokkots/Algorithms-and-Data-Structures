'''
### The following code is created without using Python's heapq. 

703. Kth Largest Element In A Stream
Easy

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


'''
from typing import List


class Node:
    def __init__(self, value=0, nxt=None, prv=None):
        self.val = value
        self.nxt = nxt
        self.prv = prv

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        
    def add(self, val: int) -> int:
        ...
