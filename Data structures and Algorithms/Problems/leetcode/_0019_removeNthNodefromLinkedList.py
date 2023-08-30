# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## naive/inefficient answer:
        counter = 0
        previous_node = second_tail = tail = head
        while tail:         # O(N)
            counter += 1
            tail = tail.next
        if counter == 1:
            return None

        node_number = counter - n 
        counter_two = 0

        while second_tail:
            if node_number == 0:
                head = head.next
            if counter_two == node_number:
                previous_node.next = second_tail.next
                break
            previous_node = second_tail
            counter_two += 1
            second_tail = second_tail.next
        return head