'''
Are similar?

Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example 1:

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
solution(a, b) = true.

The arrays are equal, no need to swap any elements.

Example 2:
For a = [1, 2, 3] and b = [2, 1, 3], the output should be
solution(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

Example 3:
For a = [1, 2, 2] and b = [2, 1, 1], the output should be
solution(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.


'''
def solution(a, b):
    if len(a) != len(b):
        return False
    swap_index = 0
    counter = 1
    for i in range(len(a)):
        if a[i] != b[i] and counter == 1:
            swap_index = i
            counter -= 1
            continue
        if a[i] != b[i] and counter == 0:
            a[swap_index], a[i] = a[i], a[swap_index]
            counter -= 1
            continue
            
    return a == b