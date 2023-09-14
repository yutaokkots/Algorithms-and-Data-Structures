'''
25. Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1. 
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2. 
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
from ListNode import ListNode
from typing import Optional

NODE_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def linkedListGenerator(lst):
    head = node = ListNode(lst[0])
    for i in range(len(lst)):
        if i == 0:
            continue
        node.next = ListNode(lst[i])
        node = node.next
    return head

def linkedListReader(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result



class Solution:
    '''
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
        
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    ''' 


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = previousGroup = ListNode(next=head)
        while True:
            kth_node = self.get_kth_node(previousGroup, k)
            if kth_node is None:
                break
            nextGroup = kth_node.next
            current, previous = previousGroup.next, nextGroup
            while nextGroup != current:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            
            tmp = previousGroup.next

            previousGroup.next = kth_node
            previousGroup = tmp
            
        return dummy.next
    
    def get_kth_node(self, start_node, k):
        while start_node and k > 0:
            start_node = start_node.next
            k -= 1

        return start_node


head_1 = linkedListGenerator(NODE_1)

sol = Solution()
head_1_processed = sol.reverseKGroup(head=head_1, k=3)

print(linkedListReader(head_1_processed))