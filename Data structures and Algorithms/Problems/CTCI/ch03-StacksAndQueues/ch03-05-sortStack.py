# Write a program to sort a stack such that the smallest items are on top. 
# you can use an additional temporary stack, but you may not copy the elements
# into any other data structure (such as an array)
# The stack supports the following operations:
# push
# pop
# peek
# isEmpty

class SortStack():
    def __init__(self):
        self.main_stack = []
        self.temp_stack = []

    def sort(self, val:int):
        # [5, 4, 3, 2]
        # [2, 3, 4, 5]
        # [2, 3, 4, 5, 1]
        # 1
        while self.main_stack:
            popped_element = self.main_stack.pop()
            self.temp_stack.append(popped_element)
        self.temp_stack.append(val)
        print(self.temp_stack)
        while self.temp_stack:
            if len(self.temp_stack) < 2:
                self.main_stack.append(self.temp_stack.pop())
                break
            curr_val = self.temp_stack.pop()
            next_val = self.temp_stack.pop()
            if curr_val < next_val:
                self.main_stack.append(next_val)
                self.temp_stack.append(curr_val)
            else:
                self.main_stack.append(curr_val)
                self.main_stack.append(next_val)


    def push(self, val:int):
        self.sort(val)

    def pop(self) -> int:
        if self.main_stack == []:
            return -1
        return self.main_stack.pop()

    def peek(self) -> int:
        print(self.main_stack)

    def isEmpty(self) -> bool:
        return len(self.main_stack) == 0

sort_stack = SortStack()
sort_stack.push(5)
sort_stack.push(4)
sort_stack.push(6)
sort_stack.push(2)
sort_stack.push(3)
sort_stack.push(9)
sort_stack.push(7)
print(f"main: {sort_stack.main_stack}, temp: {sort_stack.temp_stack}")
a = sort_stack.pop()
b = sort_stack.pop()
c = sort_stack.pop()

print(f"a: {a}, b: {b}, c: {c}")

sort_stack.peek()

print(f"is empty?: {sort_stack.isEmpty()}")
sort_stack.pop()
print(f"is empty?: {sort_stack.isEmpty()}")
sort_stack.pop()
print(f"is empty?: {sort_stack.isEmpty()}")
sort_stack.pop()
print(f"is empty?: {sort_stack.isEmpty()}")
sort_stack.pop()
print(f"is empty?: {sort_stack.isEmpty()}")
sort_stack.pop()
print(f"is empty?: {sort_stack.isEmpty()}")
