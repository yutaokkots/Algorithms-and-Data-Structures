# Given an array of integers heights representing the histogram's bar height 
# where the width of each bar is 1, return the area of the largest rectangle in the histogram.

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = [] # pair of elements, [index, height]

        for i, h in enumerate(heights):
            start = i
            # while the stack is not empty, 
            # and the current height is greater than the last item of the stack's height
            while stack and stack[-1][1] > h:
                # destructure the popped item 
                index, height = stack.pop()
                #check if this popped stack could be the largest rectangle
                # compare current maxArea, and area (height x (i - index))
                maxArea = max(maxArea, height * (i - index))
                # because we know that this popped height, 'height', is greater than the current height, 'h'
                # we can extend the start index, 'start', to the index that was just popped, 'index'
                start = index
                # when adding the current index and height [index, height],
                # instead of adding the current index, use the 'start' index that was reassigned above. 
                stack.append((start, h))
            #still compute the heights for items left in histogram
            for i, h in stack:
                maxArea = max(maxArea, h * (len(heights) - i))

        # maxArea = 0
        # stack = []

        # for i, h in enumerate(heights):
        #     start = i
        #     while stack and stack[-1][1] > h:
        #         index, height = stack.pop()
        #         maxArea = max(maxArea, height * (i - index))
        #         start = index
        #     stack.append((start, h))
        # for i, h in stack:
        #     maxArea = max(maxArea, h * (len(heights) - i))
        # return maxArea

    def largestRectangleArea2(self, heights: list[int]) -> int:
        stack, result = [], 0
        for h in heights + [-1]:
            step = 0
            while stack and stack[-1][1] >= h:
                w, h = stack.pop()
                step += w
                result = max(result, step * h)
            stack.append((step + 1), h)

        return result

h1 = [2,1,5,6,2,3]
h2 = [2,4]



sol = Solution()
print(sol.largestRectangleArea(h1))
print(sol.largestRectangleArea(h2))