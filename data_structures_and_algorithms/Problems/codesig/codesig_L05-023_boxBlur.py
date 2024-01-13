'''
Box Blur

The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: 
Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. 
All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.

Example 1:
image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]

solution(image) = [[1]].

Example 2:
image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]

solution(image) = [[5, 4], 
                   [4, 4]]

Example 3:
image = [[36,0,18,9], 
         [27,54,9,0], 
         [81,63,72,45]]

solution(image) = [[40,30]] 

Example 4:
image = [[36,0,18,9,9,45,27], 
         [27,0,254,9,0,63,90], 
         [81,255,72,45,18,27,0], 
         [0,0,9,81,27,18,45], 
         [45,45,227,227,90,81,72], 
         [45,18,9,255,9,18,45], 
         [27,81,36,127,255,72,81]]

solution(image) = [[82,73,48,25,31], 
                   [77,80,57,32,32], 
                   [81,106,88,68,42], 
                   [44,96,103,89,45], 
                   [59,113,137,126,80]]
'''

def solution(image):
    rows, cols = len(image), len(image[0])
    directions = [(-1,-1), (-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    answer = []
    for row in range(1, rows - 1):
        new_row = []
        for col in range(1, cols - 1):
            summation = image[row][col]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                summation += image[r][c]
            avg = summation // 9
            new_row.append(avg)
        answer.append(new_row)
        
    return answer
        