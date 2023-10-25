'''

Shape area

Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

Example

For n = 2, the output should be
solution(n) = 5;
For n = 3, the output should be
solution(n) = 13.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
1 ≤ n < 104.

[output] integer

The area of the n-interesting polygon.

3 -> 13
4 -> 25
5 -> 41
100 -> 19801
7000 -> 97986001
8000 -> 127984001
9998 -> 199900013
'''

def solution(n):
    base = side = 2 * n - 1 
    sides = 0
    while side > 1:
        sides += (side - 2) * 2
        side -= 2 
    return base + sides 