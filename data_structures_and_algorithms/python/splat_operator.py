"""
The Splat Operator

'*' unpacks the contents. 

example -> used in *args
"""

"""splat operator on a 2-D matrix."""
grid1 = [[3,1,2,2],
         [1,4,4,5],
         [2,4,2,2],
         [2,4,2,2]]
print(grid1)
# [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]

print(*grid1)           #splat operator
# [3, 1, 2, 2] [1, 4, 4, 5] [2, 4, 2, 2] [2, 4, 2, 2]

"""splat operator on a list."""
contents = ["a", "b", "c"]
print(contents)
# ['a', 'b', 'c']

print(*contents)        #splat operator
# a b c
