# Given an list of elements, how to iterate over the array both backwards and fowards at the same time
# and, for example, accumulate the sum of the values backwards and fowards simultaneously?

nums = [1, 2, 3, 4, 5, 6]
f_accum = 0
b_accum = 0
f_cumulative = []
b_cumulative = []
# ideal result:
# f_cumulative = [0, 1, 3, 6, 10, 15, 21]
# b_cumulative = [21, 20, 18, 15, 11, 6, 0]
def f_accumulator(nums):
    f_accum = 0
    f_cumulative = []
    for i in range(len(nums)):
        f_accum += nums[i]
        f_cumulative.append(f_accum)
    return f_cumulative
#print(f_accumulator(nums))

# O{N^2} solution, times out. 
def accumulator(nums):
    i = 0
    length = len(nums)
    f_accum = 0
    b_accum = 0
    f_cumulative = [0]
    b_cumulative = [0]
    while i < length:
        f_accum += nums[i]
        f_cumulative.append(f_accum)
        b_accum += nums[length - i - 1]
        b_cumulative.append(b_accum)
        #print(length - i - 1)
        i += 1

    return f_cumulative, b_cumulative[::-1]

nums_cumulative_forward, nums_cumulative_backward = accumulator(nums)
print(nums_cumulative_forward)
print(nums_cumulative_backward)