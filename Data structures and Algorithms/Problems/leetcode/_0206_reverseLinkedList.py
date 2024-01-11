"""206. Reverse Linked List"""

'''
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 

Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000
 
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        return prev

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Purpose: output the input linked list in reverse
        # linked list can be empty
        # number of nodes can be up to 5000
        # the value of the nodes is between -5000 and + 5000

        #edge case where head is empty
        if not head:
            return head

        # create the first Node 
        new_node = ListNode(head.val)

        #[1, 2, 3, 4, 5]
        while head.next != None:
            head = head.next
            new_node = ListNode(head.val, new_node) 

        # specify returning:
        return new_node
    
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        previous_head = None
        while head.next != None:
            next_ = head.next    
            head.next = previous_head
            previous_head = head  
            head = next_            
        head.next = previous_head
        return head

    def reverseList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    

    def reverseList4(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return newHead