# Divide and Conquer are recursive algorithms
# Two steps:
# 1. Figure out the base case. This should be the simplest possible case.
# 2. Divide or decrease your problem until it becomes the base case.


# Examples
# quick sort

# Example 1 - - - - - - - - - - -
# Given an array of numbers, add up all of the numbers and return the total
# Non recrusive algorithm:
def sum(arr):
    sum = 0
    for n in arr:
        sum += n
    return sum

array_of_numbers = [2, 4, 6]

total_1 = sum(array_of_numbers)
print(total_1)

# Recursive algorithm:
def sum_recursive(arr, i = 0, sum=0):
    if i == len(arr) - 1:
        return sum + arr[i]
    total = sum_recursive(arr, i + 1, sum+arr[i])
    return total

total_2 = sum_recursive(array_of_numbers)
print(total_2)

def sum_recursive_2(arr, i=0):
    if i == len(arr):
        return 0
    return arr[i] + sum_recursive(arr, i + 1)

total_3 = sum_recursive_2(array_of_numbers)
print(total_3)

# Example 2.
# Write a recursive function to count the number of items in a list 
def count_array_recursively(arr, i = 0):
    if i == len(arr) - 1:
        return 1
    return 1 + count_array_recursively(arr, i + 1)

array_of_numbers_test_size = [2, 4, 6, 8, 12, 3, 2, 5, 0, 2]
size = count_array_recursively(array_of_numbers_test_size)
print(size)

# Example 3.
# Find the maximum number in a list.
def max_array_recursively(arr, i = 0, maximum=0):
    if i == len(arr) - 1:
        return maximum
    maximum = max(maximum, arr[i])
    return max_array_recursively(arr, i+1, maximum)

array_of_numbers_test_max = [2, 4, 6, 8, 9, 3, -2, 5, 0, 2]
max_value = max_array_recursively(array_of_numbers_test_max)
print(max_value)