from typing import Optional, List, ListNode

# 141. Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# for the following examples, 'pos' is not an input
# example 1
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# example 2
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# example3
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

class Solution:
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        memo = []
        if not head or not head.next:
            return False
        while head.next:
            if id(head) not in memo:
                memo.append(id(head))
            else:
                return True
            head = head.next
        return False
    
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        # two pointer approach, fast and slow pointers
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
    
    def hasCycle3(self, head: Optional[ListNode]) -> bool:
        pointer_1 = pointer_2 = head
        while pointer_2 and pointer_2.next:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next.next
            if pointer_1 == pointer_2:
                return True
        return False
    

    def hasCycle4(self, head: Optional[ListNode]) -> bool:
        memo = {}
        while head:
            memo[head] = 1 + memo.setdefault(head, 0)
            if memo[head] > 1:
                return True

            head = head.next
        return False
