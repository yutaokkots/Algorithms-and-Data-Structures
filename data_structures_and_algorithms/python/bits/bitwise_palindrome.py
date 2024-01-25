"""operation >> and <<"""

"""Use the bitwise shift operators to determine if a series of integers is a palindrome. 
See LC1457 for implementation.
"""

from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree_node = TreeNode(4)

print(1 << tree_node.val)
# 16
# Calculates 2**x
# 2 ** 4 => 16

print(1 >> tree_node.val)
# 0

print(f"1 << 1: {1 << 1}")
print(f"1 << 2: {1 << 2}")
print(f"1 << 3: {1 << 3}")
print(f"1 << 4: {1 << 4}")
print(f"1 << 5: {1 << 5}")
print(f"1 << 6: {1 << 6}")

def bitwise_palindrome(nums: List[int]) -> None:
    x = 0
    print(nums)
    for n in nums:
        j = 1 << n
        x ^= j
        #print(f". . .\n{j} = 1 << n\nx ^= 1 << n, x => {x}\nx.bit_count() = {x.bit_count()}\nx.bit_count() <= 1: {x.bit_count() <= 1}")
    print(f"palindrome: {x.bit_count() <= 1}")
    print("\n")
        
nums_lst01 =[1, 2, 2, 1]
bitwise_palindrome(nums_lst01)
# [1, 2, 2, 1]
    # . . .
# 2 = 1 << n        <- 2 ** 1
# x ^= 1 << n, x => 2
# x.bit_count() = 1
# x.bit_count() <= 1: True
    # . . .
# 4 = 1 << n        <- 2 ** 2
# x ^= 1 << n, x => 6
#       2:  0 0 1 0 <- value of prev x
#   XOR 4:  0 1 0 0 <- value of '1 << n'
#           0 1 1 0 <- 6
# x.bit_count() = 2
# x.bit_count() <= 1: False
    # . . .
# 4 = 1 << n        <- 2 ** 2
# x ^= 1 << n, x => 2
#       6:  0 1 1 0 <- value of prev x
#   XOR 4:  0 1 0 0 <- value of '1 << n'
#           0 0 1 0 <- 2
# x.bit_count() = 1
# x.bit_count() <= 1: True
    # . . .
# 2 = 1 << n        <- 2 ** 1
# x ^= 1 << n, x => 0
#       2:  0 0 1 0 <- value of prev x
#   XOR 2:  0 0 1 0 <- value of '1 << n'
#           0 0 0 0 <- 0
# x.bit_count() = 0
# x.bit_count() <= 1: True

nums_lst02 =[1, 2, 1, 13]
bitwise_palindrome(nums_lst02)
# [1, 2, 1, 13]
# . . .
# 2 = 1 << n
# x ^= 1 << n, x => 2
# x.bit_count() = 1
# x.bit_count() <= 1: True
# . . .
# 4 = 1 << n
# x ^= 1 << n, x => 6
# x.bit_count() = 2
# x.bit_count() <= 1: False
# . . .
# 2 = 1 << n
# x ^= 1 << n, x => 4
# x.bit_count() = 1
# x.bit_count() <= 1: True
# . . .
# 8192 = 1 << n
# x ^= 1 << n, x => 8196
#          4: 00000000000100 <- valuue of prev x
#   XOR 8192: 10000000000000 <- value of '1 << n'
#             10000000000100 <- 8196
# x.bit_count() = 2
# x.bit_count() <= 1: False


nums_lst03 =[2, 2, 5, 5]
bitwise_palindrome(nums_lst03)
# [2, 2, 5, 5]
# . . .
# 4 = 1 << n
# x ^= 1 << n, x => 4
# x.bit_count() = 1
# x.bit_count() <= 1: True
# . . .
# 4 = 1 << n
# x ^= 1 << n, x => 0
# x.bit_count() = 0
# x.bit_count() <= 1: True
# . . .
# 32 = 1 << n
# x ^= 1 << n, x => 32
# x.bit_count() = 1
# x.bit_count() <= 1: True
# . . .
# 32 = 1 << n
# x ^= 1 << n, x => 0
# x.bit_count() = 0
# x.bit_count() <= 1: True

nums_lst04 =[1, 2, 2, 5, 5]
bitwise_palindrome(nums_lst04)
# [1, 2, 2, 5, 5]
# . . .
# 2 = 1 << n
# x ^= 1 << n, x => 2
# x.bit_count() = 1
# x.bit_count() <= 1: True
# . . .
# 4 = 1 << n
# x ^= 1 << n, x => 6
# x.bit_count() = 2
# x.bit_count() <= 1: False
# . . .
# 4 = 1 << n
# x ^= 1 << n, x => 2
# x.bit_count() = 1
# x.bit_count() <= 1: True
# . . .
# 32 = 1 << n
# x ^= 1 << n, x => 34
# x.bit_count() = 2
# x.bit_count() <= 1: False
# . . .
# 32 = 1 << n
# x ^= 1 << n, x => 2
# x.bit_count() = 1
# x.bit_count() <= 1: True