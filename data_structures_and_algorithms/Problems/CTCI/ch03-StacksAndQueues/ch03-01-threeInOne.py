#describe how you would use a single array to implement three stacks

# assume size = size of each stack
# assume n_stacks = total number of stacks in the array. 

class N_stack():
    def __init__(self, size, n_stacks):
            # size of each stack (number of elements)
        self.size = size
            # number of stacks
        self.n_stacks = n_stacks
            # capacity -> number of items that can fit inside each (sub) stack (same as size)
        self.stack_capacity = size

            # sizes holds the size of each stack
        self.sizes = [None] * self.n_stacks
            # example, input n_stacks = 3:
            # [None, None, None]

            #values holds the various values of the three arrays in a single stack
        self.values = [None] *  n_stacks  * self.size
            # example, input n_stacks = 3, size = 5: length = 15
            # [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]


    # 'isFull' -> check if that particular stack is full:
    def isFull(self, stack_number):
            #self.sizes holds the number of elements that are inside each stack. For example, if
            # the input 'stack_number' is 0 out of the 3, 
            # self.sizes[0] returns the current index of the last item in that stack
            # and evaluate whether self.sizes[stack_num] is equal to the self.stack_capacity (how many items can fit inside
            # a (sub) stack) 
        return self.sizes[stack_number] == self.stack_capacity

    # 'index_top()' checks for index of top element in stack, 'stack_number' -> which (sub) stack in the stacks array. 
    def index_top(self, stack_number):
            # the offset finds the offset of the start of a (sub)stack inside the array,
            #    by multiplying the stack_number x the stack_capacity (same as size of each stack)
        offset = stack_number * self.stack_capacity
            # for example: stack_capacity is 5, and stack_number is 1
            # self.values:  [None, None, None, None, None, 1, 2, None, None, None, None, None, None, None, None]
            # start pos:     ^                             ^                       ^


        size = self.sizes[stack_number]
            # self.sizes[1]:
            #   [None, None, None]
            #           ^
            # this self.sizes stores the top stack number here
            # example --> 2

            # return value. Example: if stack_number = 1
            # offset -> 5 
            # size -> 1
            # (offset + size - 1) = (5 + 2 - 1) -> 6 <- the index of the top stack

        return offset + size - 1

    # 'isEmpty()' -> checks to see if stack is empty
    def isEmpty(self, stack_number:int) -> bool:
        return self.sizes[stack_number] == 0

    # Pushes 'X' into the Mth stack.
    def push(self, stack_num:int, value:int):
        #check for capacity
        if self.isFull(stack_num):
            raise Exception("stack overflow")
        
        if self.sizes[stack_num] == None:
            self.sizes[stack_num] = 0
        self.sizes[stack_num] += 1
        self.values[self.index_top(stack_num)] = value

    # pops the top item from the Mth stack.
    def pop(self, stack_num:int): 
        if self.isEmpty(stack_num):
            raise Exception("Empty")
        top_idx = self.index_top(stack_num)
        value = self.values[top_idx]
        self.values[top_idx] = None        # clears
        self.sizes[stack_num] -= 1
        return value




nstack = N_stack(5, 3)
print(f"SIZE: {nstack.sizes}, VALUES: {nstack.values}")

nstack.push(0, 5)
print(f"SIZE: {nstack.sizes}, VALUES: {nstack.values}")

nstack.push(0, 6)
print(f"SIZE: {nstack.sizes}, VALUES: {nstack.values}")

nstack.push(1, 6)
print(f"SIZE: {nstack.sizes}, VALUES: {nstack.values}")

nstack.pop(0)
print(f"SIZE: {nstack.sizes}, VALUES: {nstack.values}")

nstack.pop(1)
print(f"SIZE: {nstack.sizes}, VALUES: {nstack.values}")

nstack.pop(1)
print(f"SIZE: {nstack.sizes}, VALUES: {nstack.values}")
