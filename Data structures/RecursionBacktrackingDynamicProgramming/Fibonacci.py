class Fib():
    def fibonacci_head(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.fibonacci_head(n - 1) + self.fibonacci_head(n - 2)
        
        # fib1 = self.fibonacci_head(n - 1)
        # fib2 = self.fibonacci_head(n - 2)

        # result = fib1 + fib2

        # return result
    
    def fibonacci_tail1(self, n, a = 0, b = 1): 
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci_tail1(n-1, a + n, b + n) + self.fibonacci_tail1(n-2, a + n, b + n)
    
    def fibonacci_tail2(self, n, a = 0, b = 1): 
        # implement the algorithm here 
        if n == 0:
            return a
        if n == 1:
            return b
        return self.fibonacci_tail2(n-1, b, a + b) 
    
fib = Fib()
result = fib.fibonacci_head(8)
print(result)
result2 = fib.fibonacci_tail1(8)
print(result2)
result3 = fib.fibonacci_tail2(8)
print(result3)

## SEVERAL STACK FRAMES are created concurrently in stack