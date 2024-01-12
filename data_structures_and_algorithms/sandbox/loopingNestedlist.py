# what is the difference between for looping and enumerating?
# ability to destructure a list of a list while looping

# values of heights in a list
heights = [2,1,5,6,2,3]
# values of heights and their index, represented by [index, height], in a variable called stack
stack = [[0,2],[1,1],[2,5],[3,6],[4,2],[5,3]]

# values of heights and their index, and another value, 'width, represented by [index, height, width], 
# in a variable called stack_with_three
stack_with_three = [[0,2,6],[1,1,3],[2,5,2],[3,6,8],[4,2,2],[5,3,1]]

for i, h in enumerate(heights):
    print(f"index: {i}; height: {h}")
# >>> index: 0; height: 2
# >>> index: 1; height: 1
# >>> index: 2; height: 5
# >>> index: 3; height: 6
# >>> index: 4; height: 2
# >>> index: 5; height: 3

for i, h in stack:
    print(f"index: {i}; height: {h}")
# >>> index: 0; height: 2
# >>> index: 1; height: 1
# >>> index: 2; height: 5
# >>> index: 3; height: 6
# >>> index: 4; height: 2
# >>> index: 5; height: 3

for i, h, w in stack_with_three:
    print(f"index: {i}; height: {h}, width: {w}")
# >>> index: 0; height: 2, width: 6
# >>> index: 1; height: 1, width: 3
# >>> index: 2; height: 5, width: 2
# >>> index: 3; height: 6, width: 8
# >>> index: 4; height: 2, width: 2
# >>> index: 5; height: 3, width: 1