# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = current = ListNode()

        remainder = 0
        while l1 or l2 or remainder:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + remainder

            remainder = val // 10
            val = val % 10
            current.next = ListNode(val)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        save = []

        def add(val1:int, val2:int, r:int) -> int:
            summation = val1 + val2 + r
            r = 0
            if summation > 19:
                summation -= 20
                r = 2
            elif summation > 9:
                summation -= 10
                r = 1
            save.append(summation)
            return r
        
        remainder = add(l1.val, l2.val, remainder)
        while l1.next != None and l2.next != None:
            l1 = l1.next
            l2 = l2.next
            remainder = add(l1.val, l2.val, remainder)

        while l1.next != None or l2.next != None:
            if l1.next:
                l1 = l1.next
                remainder = add(l1.val, 0, remainder)  
            elif l2.next:
                l2 = l2.next
                remainder = add(0, l2.val, remainder)
        remainder = add(0, 0, remainder)
        
        prev = None
        head = None
        for i, n in enumerate(save[::-1]):
            if i == 0 and n == 0:
                continue
            node = head = ListNode(n)
            if i > 0:
                node.next = prev
            prev = node

        return head