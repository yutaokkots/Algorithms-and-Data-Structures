'''
74. Search a 2D matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do a search
        row_start, row_end = 0, len(matrix) - 1
        col_start, col_end = 0, len(matrix[row_start]) - 1
        middle = None
        while row_start <= row_end:
            middle = (row_start + row_end) // 2
            if matrix[middle][col_start] <= target <= matrix[middle][col_end]:
                break
            elif target < matrix[middle][col_start]:
                row_end = middle - 1
            elif matrix[middle][col_end] < target:
                row_start = middle + 1
        
        target_lst = matrix[middle]
        while col_start <= col_end:
            mid = (col_start + col_end) // 2
            if target == target_lst[mid]:
                return True
            elif target < target_lst[mid]:
                col_end = mid - 1
            elif target > target_lst[mid]:
                col_start = mid + 1
        
        return False
    

    '''
    
    var searchMatrix = function (matrix, target) {
    const [rows, cols] = [matrix.length, matrix[0].length];
    let [left, right] = [0, rows * cols - 1];

    while (left <= right) {
        const mid = (left + right) >> 1;
        const [row, col] = [Math.floor(mid / cols), mid % cols];
        const guess = matrix[row][col];

        const isTarget = guess === target;
        if (isTarget) return true;

        const isTargetGreater = guess < target;
        if (isTargetGreater) left = mid + 1;

        const isTargetLess = target < guess;
        if (isTargetLess) right = mid - 1;
    }

    return false;
};
    
    '''