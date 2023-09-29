'''
21. Merge Two Sorted Lists
Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

'''


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ''' mergeTwoLists1 class method merges two sorted linked lists and outputs the list after merge.
        
        list1 -- a sorted linked list
        list2 -- a sorted linked list
        returns a sorted linked list
        '''
        # edge case to immediately return the list that does exist. 
        if not list1:
            return list2
        if not list2:
            return list1
        
        # instantiate the ListNode class and assign it a head_node (pointer that remains static), and inter_node (pointer that moves).
        head_node = inter_node = ListNode()
        
        # go through list1 and list2, and sort, and add the list to inter_node.
        while list1 and list2:
            if list1.val < list2.val:
                inter_node.next = list1
                list1 = list1.next
            else:
                inter_node.next = list2
                list2 = list2.next
            inter_node = inter_node.next

        # if list1 or list2 have any items remaining, add to the end of inter_node.
        if list1:
            inter_node.next = list1
        elif list2:
            inter_node.next = list2
        
        return head_node.next

class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Goal: merge two incoming linked lists into one linked list. Both incoming linked lists are sorted. 

        if not list1:
            return list2
        if not list2:
            return list1

        list3 = inter_node = ListNode()

        # list1.val = current value of list1
        # list1.next = access next node

        while list1 and list2:
            # sort algorithm
            if list1.val < list2.val:
                inter_node.next = list1
                list1, inter_node = list1.next, inter_node.next
                
            else:  #list1.val > list2.val
                inter_node.next = list2
                list2, inter_node = list2.next, inter_node.next

        if list1:
            inter_node.next = list1
        if list2: 
            inter_node.next = list2

        return list3.next
    
