# stackOfPlates:
# Image a literal stack of paltes. 
# if the stack gets too high, it might topple
# Therefore, a new stack will be created when the previous stack exceeds a threshold
# Implement a SetOfStacks that mimics this. 
# SetofStacks.push() and setOfStacks.pop() should behave identically to a single stack 
# in other words, .pop() should return the same values as it would if there were a single stack

# implement a .popAt(index:int) that performs a pop operation on a specific sub-stack


class StackOfPlates():
    def __init__(self, limit):
        self.limit = limit
        self.stacks = []
        self.stack_idx = 0
        self.curr_stack_len = 0

    def push(self, val:int):
        if self.stacks == []:
            self.stacks.append([])
        if self.curr_stack_len == self.limit:
            self.stacks.append([val])
            self.stack_idx += 1
            self.curr_stack_len = 1
        else:
            self.stacks[self.stack_idx].append(val)
            self.curr_stack_len += 1

    def pop(self) -> int:
        if self.curr_stack_len == 0 and self.stack_idx == 0:
            print("nothing in stack")
            return
        if self.curr_stack_len == 0:
            self.stacks.pop()
            self.stack_idx -= 1
            self.curr_stack_len = self.limit
        else:
            popped_element = self.stacks[self.stack_idx].pop() 
            self.curr_stack_len -= 1
            return popped_element
        
    def popAt(self, index:int):
        number = (self.stack_idx + 1) * self.curr_stack_len 
        if index > number:
            print("Error")
            return
        if index < 0:
            remainder = -(-index % self.limit)
            removal_index = -index // self.limit

        else: 
            remainder = index % self.limit
            removal_index = index // self.limit
            
        popped_element = self.stacks[removal_index].pop(remainder)
        if self.stacks[removal_index + 1] and len(self.stacks[removal_index]) < self.limit:
            self.shift(removal_index)
        return popped_element

    def shift(self, rem_idx:int):
        while len(self.stacks[rem_idx]) < self.limit:
            if rem_idx + 1 > self.stack_idx:
                break
            removed_element = self.stacks[rem_idx + 1].pop(0)
            self.stacks[rem_idx].append(removed_element)
            if len(self.stacks[rem_idx]) == self.limit:
                rem_idx += 1

            

    
stackPlates = StackOfPlates(10)

for i in range(1, 39):
    stackPlates.push(i)
    
print(*stackPlates.stacks)

# for i in range(31):
#     stackPlates.pop()

# print(*stackPlates.stacks)

# for i in range(11):
#     stackPlates.pop()

# print(*stackPlates.stacks)

stackPlates.popAt(28)
stackPlates.popAt(12)
stackPlates.popAt(4)
stackPlates.popAt(4)
stackPlates.popAt(4)
stackPlates.popAt(4)
stackPlates.popAt(4)
stackPlates.popAt(4)
stackPlates.popAt(4)
stackPlates.popAt(4)
stackPlates.popAt(4)
# stackPlates.popAt(-5)

print(*stackPlates.stacks)