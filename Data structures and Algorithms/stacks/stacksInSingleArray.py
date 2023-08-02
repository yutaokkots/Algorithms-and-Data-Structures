# Multiple stacks in a single array. 
#
class N_stack():
    def __init__(self, n_stack, stack_length):
        self.stack_n = n_stack
        self.stack_size = stack_length
        self.stack_capacity = self.stack_size

        self.stack_ref = self.stack_n * [None]
        self.stack_values = self.stack_n * self.stack_size * [None]

        # 5
        # [#, 2, #]
        # [#, #, #, #, #, 1, #, #, #, #, #, #, #, #, #]

    def isFull(self, n_stack) -> bool:
        return self.stack_ref[n_stack] == self.stack_capacity
        
    def isEmpty(self, n_stack) -> bool:
        return self.stack_ref[n_stack] == None


    def push(self, n_stack, value):
        if self.isFull(n_stack):
            raise Exception("stack overflow")
    
        shift = self.stack_size * n_stack
        idx = self.stack_ref[n_stack] if self.stack_ref[n_stack] != None else 0
        if self.stack_ref[n_stack] == None:
            self.stack_ref[n_stack] = 0
        self.stack_ref[n_stack] += 1

        self.stack_values[idx + shift] = value

    def pop(self, n_stack) -> int:
        if self.isEmpty(n_stack):
            raise Exception("stack empty")
        stack_idx = self.stack_ref[n_stack]    
        self.stack_ref[n_stack] -= 1
        shift = n_stack * self.stack_size
        val = self.stack_values[stack_idx + shift - 1]
        self.stack_values[stack_idx + shift - 1] = None
        return val

nstack = N_stack(4, 12)
nstack.push(2, 5)
nstack.push(2, 5)
nstack.push(2, 5)
nstack.push(2, 6)
nstack.push(2, 9)
nstack.push(2, 23)
print(nstack.stack_values)
nstack.pop(2)
nstack.pop(2)
nstack.pop(2)

print(nstack.stack_values)


# [None, None, None, None, None, None, None, None, None, None, None, None, 
#  None, None, None, None, None, None, None, None, None, None, None, None,
#  5,    5,    5,    6,    None, None, None, None, None, None, None, None, 
#  None, None, None, None, None, None, None, None, None, None, None, None]