# recursion is at the center of computer science
# 
# define base-cases to avoid infinite loops
# every problem can be solved with iteration or recursion
#

class RecursionOrIteration():
    def iteration_sum(self, n):
        result = 0
        for num in range(n + 1):
            result += num
        return result
    
    def recursion_sum(self, n):
        if n == 0:
            return 0
        return n + self.recursion_sum(n - 1)

rec = RecursionOrIteration()
value_1 = rec.recursion_sum(5)
value_2 = rec.iteration_sum(5)
print(value_1)
print(value_2)

## Two types of recursion
# TAIL recursion
# - recursive function call occurs at the end of the function
# - SIMILAR to a ** for-loop or while-loop **
# - executes all statements before jumping to the next recursive call

# HEAD recursion
# - recursive function call occurs at the beginning of the function
# - saves the state of the function call before jumping into the next recursive call
# - needs more memory, because of the states it stores

class TailOrHead():
    def tail(self, n):
        # base-case
        if n == 1:
            return
        # do something
        print(n)
        ### recursive call ###
        self.tail(n - 1)
    
        ## SIMILAR TO:
        # for n in range(n):
        #     print(n)
        # while n > 1:
        #     print(n)
        #     n -= 1

    def head(self, n):
        # base-case
        if n == 1:
            return
        ### recursive call ### saves the state of the function call before jumping into the next recursive call
        self.head(n - 1)
        # do something
        print(n)

    def head_demonstration(self, n):
        print(f"Before the recursive call number {n}")
        if n == 0:
            return
        self.head_demonstration(n - 1)
        print(f"After the recursive call number {n}")

toh = TailOrHead()
toh.tail(5)
# 5
# 4
# 3
# 2
toh.head(5)
# 2
# 3
# 4
# 5   
#    
# toh.head_demonstration(5)  
# Before the recursive call number 5
# Before the recursive call number 4
# Before the recursive call number 3
# Before the recursive call number 2
# Before the recursive call number 1
# Before the recursive call number 0
# After the recursive call number 1
# After the recursive call number 2
# After the recursive call number 3
# After the recursive call number 4
# After the recursive call number 5

class Factorial():
    def factorial_head(self, n):
        # base-case
        if n == 0:
            return 1
        
        # recursive function
        result1 = self.factorial_head(n - 1)

        # do something
        result2 = n * result1
        return result2
    
    def factorial_tail(self, n, accumulator=1):
        if n == 1:
            return accumulator
        
        return self.factorial_tail(n - 1, n * accumulator)
        # n = 4, acc = 1        <- factorial_tail(4)
        # n = 3, acc = 4
        # n = 2, acc = 12
        # n = 1, acc = 24



fac = Factorial()
result = fac.factorial_tail(5)

print(result)