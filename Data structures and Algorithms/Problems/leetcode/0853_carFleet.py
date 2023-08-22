class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [[p, s] for p, s in zip (position, speed)]
        stack = []

        for p, s in sorted(pair)[:: -1]: # reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

    def carFleet1(self, target: int, position: list[int], speed: list[int]) -> int:
        car_info = []

        for i, p in enumerate(position):
            d = target - p
            car_info.append((d, d / speed[i]))

        car_info.sort()

        stack = []
        
        for car in car_info:
            if stack == []:
                stack.append(car)
            if stack and car[1] > stack[-1][1]:
                stack.append(car)
            else:
                continue

        return len(stack)

t = [3, 5, 2]
p = [3, 2, 1]

sol = Solution()
sol.carFleet()


        # target = 12
        # [10,8, 0, 5,3] <- position, 
        # [2, 4, 1, 1,3] <- speed
        # [2, 4,12, 7,9] <- distance
        # [1, 1,12, 7,3]
        #sorted
        # distance:
        # [12,9, 7, 4,  2] <- distance
        # [0, 3, 5, 8, 10] -> 12
        # [1, 3, 1, 4,  2] <- speed
        # [12,3, 7, 1,  1] <- time
        #  speed = distance / time
        #   distance / speed = time
        # 