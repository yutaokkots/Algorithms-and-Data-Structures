## Queue Via Stacks

## Impelment a MyQueue class which implements a queue using two stacks

from typing import List

class MyQueue:
    def __init__(self):
        self.stack_A = []
        self.stack_B = []

    def reset_for_append(self):
        while self.stack_B:
            self.stack_A.append(self.stack_B.pop())

    def reset_for_pop(self):
        while self.stack_A:
            self.stack_B.append(self.stack_A.pop())

    def add_list(self, new_list:List[int]):
        self.reset_for_append()
        if self.stack_A == [] and self.stack_B == []:
            self.stack_A = new_list[:]
        else:
            for n in new_list:
                self.stack_A.append(n)

    def add_item(self, new_item:int):
        self.reset_for_append()
        self.stack_A.append(new_item)

    def get_item(self) -> int:
        self.reset_for_pop()
        return self.stack_B.pop()
    

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
q = MyQueue()

q.add_list(sample_list)
print(f"--> stack_A: {q.stack_A}, stack_B: {q.stack_B}")

for _ in range(4):
    q_item = q.get_item()
    print(f"--> stack_A: {q.stack_A}, stack_B: {q.stack_B}")
    print(f"next queue item: {q_item}")

for n in range(-1, -5, -1):
    q.add_item(n)
    print(f"--> stack_A: {q.stack_A}, stack_B: {q.stack_B}")

for _ in range(8):
    q_item = q.get_item()
    print(f"--> stack_A: {q.stack_A}, stack_B: {q.stack_B}")
    print(f"next queue item: {q_item}")

sample_list_2 = [11, 12, 13, 14, 15]

q.add_list(sample_list_2)
print(f"--> stack_A: {q.stack_A}, stack_B: {q.stack_B}")