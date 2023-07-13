class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [[p, s] for p, s in zip (position, speed)]
        stack = []

        for p, s in sorted(pair)[:: -1]: # reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)


t = [3, 5, 2]
p = [3, 2, 1]

sol = Solution()
sol.carFleet()
