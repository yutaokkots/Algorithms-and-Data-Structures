# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import ListNode

class Solution:
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
    

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return newHead