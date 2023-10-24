'''
Matrix Elements Sum

A rectangular matrix of 0 or positive integers is provided, representing a 2-dimensional building.
The 0th index of the matrix (row) represents the top, and the matrix.length - 1 index of the matrix represents the bottom of the building. 

The i'th index of each row in the matrix represents the cost of a unit of the building. However, if the cost of a unit is 0, then that unit and any other unit below is not counted. 

Given a rectangular matrix, return the total cost of the units in the building. 

Example 1:
input = [[0, 1, 1, 2], 
         [0, 5, 0, 0], 
         [2, 0, 3, 3]]
output = 9
Reason:
input = [[0, 1, 1, 2], 
         [0, 5, 0, 0], 
         [X, 0, X, X]]


Example 2:
input =  [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]
output = 9
Reason:
input =  [[1, 1, 1, 0], 
          [0, 5, 0, X], 
          [X, 1, X, X]]

Example 3:
input = [[4, 0, 1], 
         [10,7, 0], 
         [0, 0, 0], 
         [9, 1, 2]]
output = 15

Example 4:
input = [[1,1,1], 
         [2,2,2], 
         [3,3,3]]
output = 18
'''

def solution(matrix):
    haunted = []
    cost = 0
    rows, cols = len(matrix), len(matrix[0])
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                haunted.append(c)
            elif c not in haunted:
                cost += matrix[r][c]
    return cost