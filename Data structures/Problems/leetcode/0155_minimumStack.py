# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

#You must implement a solution with O(1) time complexity for each function.

class MinStack:

    def __init__(self):
        #O(1) time complexity for each method. 

        self.stack = []
        # self.stack = [-2, 0, -3, 1, -4]

        # dict sort (O(N))
        # min-heap (O(LogN))
        # reference(s): 1-pointer or 2-pointer

        # reference = (2 ** 31) - 1
        self.min_stack = []
        # self.min_stack = [-2, -2, -3, -3, -4]
        #

    def push(self, val: int) -> None:
        # push a value, 'val' into the stack
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        # remove the last item in the stack
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # return the last item in the stack
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        # return the minimum value in the stack