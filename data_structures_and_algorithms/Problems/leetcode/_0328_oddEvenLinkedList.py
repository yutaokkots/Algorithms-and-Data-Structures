"""328. Odd Even Linked List"""

"""
328. Odd Even Linked List
Medium

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 
Constraints:
    The number of nodes in the linked list is in the range [0, 10^4].
    -106 <= Node.val <= 10^6
"""
from typing import Optional
from ListNode import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """Solution class for LC328."""
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node = head
        count = 0
        odd_head = odd = None
        even_head = even = None

        while node:
            count += 1
            if count == 1:
                odd_head = node
                odd = node
                node = node.next
                continue
            if count == 2:
                even_head = node
                even = node
                node = node.next
                continue
            if count % 2 == 1:
                odd.next = node
                odd = node
            elif count % 2 == 0:
                even.next = node
                even = node
            node = node.next
        odd.next = even_head
        if even:
            even.next = None
        return odd_head
    
class Solution2:
    """Solution class for LC328, adapted into python, originally Java code by @03yadavankit."""
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even_head = even = head.next
        while (even and even.next and 
                odd and odd.next):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head