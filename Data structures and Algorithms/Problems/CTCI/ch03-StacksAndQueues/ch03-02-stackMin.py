# Stack Min
# How would you design a stack, which in addition to push and pop,
# has a function 'min()' that returns the minimum element?
# push(), pop(), and min() should all operate in O(1) time

from typing import List
class StackMin():
    def __init__(self):
        self.stack = []
        self.min = None

    def createStack(self, nums:List[int]):
        for i in range(len(nums)):
            if self.min is None:
                self.min = nums[i]
            else:
                self.min = min(self.min, nums[i])
            self.stack.append(nums[i])
        print(*self.stack)
        print(f"current min: {self.min}")
    
    def push(self, val:int):
        if self.min is None:
            self.min = val
        else:
            self.min = min(self.min, val)
        self.stack.append(val)
        print(*self.stack)

    def pop(self):
        if self.stack == []:
            print("error")
            return
        popped_value = self.stack.pop()
        print(*self.stack)
        return popped_value

    def minimum(self):
        print(f"current min: {self.min}")
        
    
lst_1 = [4, 5, 2, 3, 2, 6, 8, -5, -2, -6, -3, -8, 9]

minstack = StackMin()

#minstack.createStack(lst_1)

minstack.push(-9)
minstack.push(9)
minstack.push(-2)
minstack.push(2)
minstack.minimum()
minstack.push(5)
minstack.pop()
minstack.push(-12)
minstack.minimum()