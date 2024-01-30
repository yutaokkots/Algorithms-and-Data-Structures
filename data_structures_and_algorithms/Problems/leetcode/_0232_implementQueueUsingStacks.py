"""Implement Queue Using Stacks"""

"""
Implement Queue Using Stacks
Easy

Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 
Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

Constraints:
    1 <= x <= 9
    At most 100 calls will be made to push, pop, peek, and empty.
    All the calls to pop and peek are valid.

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? 
In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
"""

class MyQueue:
    """Solution for LC232 using two stacks to transfer between."""
    def __init__(self):
        self.q = []
        self.cache = []
        self.length = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.length += 1

    def pop(self) -> int:
        if self.q:
            self.transfer(self.q, self.cache)
            item = self.cache.pop()
            self.length -= 1
            self.transfer(self.cache, self.q)
            return item

    def peek(self) -> int:
        if self.q:
            return self.q[0]

    def empty(self) -> bool:
        return False if self.length > 0 else True

    def transfer(self, source_lst, dest_lst) -> None:
        while source_lst:
            dest_lst.append(source_lst.pop())

class MyQueue2:
    """First naive implementation of LC232."""
    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        item = None
        if self.q:
            item = self.q.pop(0)
        return item

    def peek(self) -> int:
        if self.q:
            return self.q[0]

    def empty(self) -> bool:
        return False if self.q else True