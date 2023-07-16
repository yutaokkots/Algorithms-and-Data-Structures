# using modulo to shift a list

class Solution():
    def rotateRight(self, array):
        result = [0]*len(array)
        for n in range(len(array)):
            # current number, n 
            # n + 1 -> one number higher than n
            # n + 1 % len(result) -> if (n + 1) < len(result), then returns n+1
            result[(n + 1) % len(result)] = array[n]
        return result
    

sol = Solution()
arr = [1, 2, 3, 4, 5]
arr = sol.rotateRight(arr)
print(arr)
arr = sol.rotateRight(arr)
print(arr)
arr = sol.rotateRight(arr)
print(arr)
arr = sol.rotateRight(arr)
print(arr)
arr = sol.rotateRight(arr)
print(arr)