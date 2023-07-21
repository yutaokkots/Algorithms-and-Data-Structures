# Quicksort
# * uses Divide and Conquer -> recursive
# * time complexity depends on pivot
# Generally, average case -> O(nlogn).. but worst case -> O(n^2)

# base case:
# just return arrays with one element or no elements (empty)

#           if len(array < 2:
#               return array)

# Use a pivot:
# original array -> [33, 15, 10]
# example, use first element as pivot <33>. 
# Following is called 'partitioning'
# 
# [15, 10] <33> [] 
#    |      |   |
#    |      |  numbers greater than pivot (empty)
#    |     pivot
#   numbers smaller than pivot
# 
# Steps for Quick Sort
# 1. Pick a pivot.
# 2. Partition the array into two sub-arrays: 
#    elements less than the pivot and elements greater than the pivot.
# 3. Call quicksort recursively on the two sub-arrays.

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
quicksort_list = [10, 5, 2, 3, 4, 7]

result = quicksort(quicksort_list)
print(result)

# The time complexity of quicksort is unique because it depends on the pivot chosen. 
# The performance of the quicksort heavily depends on the pivot you choose. 
# Using a pivot at the beginning of the array is O(n)
# using a pivot at the middle of the array is O(logn)