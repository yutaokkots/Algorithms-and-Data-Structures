#143 
#You are given the head of a singly linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tail = head
        memo = {}
        right = 0
        while tail:
            memo[right] = tail
            right += 1
            tail = tail.next
        right -= 1
        left = 0
        while left < right:
            memo[left].next = memo[right]
            left += 1
            memo[right].next = memo[left]
            right -= 1
            memo[left].next = None

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # using FAST and SLOW pointers
git 
        
