'''
Sort by Height
Rearrange the numbers in the list, a, in a non-descending order without moving the position of the negative integers where a[i] = -1:

Example 1:
For a = [-1, 150, 190, 170, -1, -1, 160, 180], 
output = [-1, 150, 160, 170, -1, -1, 180, 190].

Example 2:
a : [-1, -1, -1, -1, -1]
output: [-1, -1, -1, -1, -1]

Example 3:
a: [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
output: [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]


If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.

Guaranteed constraints:
1 ≤ a.length ≤ 1000,
-1 ≤ a[i] ≤ 1000.

'''
example_1 = [-1, 150, 190, 170, -1, -1, 160, 180]

def solution(a):
    heights = [n for n in a if n > 0]
    heights.sort()
    counter = 0
    for i in range(len(a)):
        if a[i] > 0:
            a[i] = heights[counter]
            counter += 1
    return a

print(solution(example_1))