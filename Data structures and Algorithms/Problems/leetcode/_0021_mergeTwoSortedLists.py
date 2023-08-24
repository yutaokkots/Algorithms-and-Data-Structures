# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
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
    
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head_node = inter_node =  ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                inter_node.next = list1
                list1 = list1.next
            else:
                inter_node.next = list2
                list2 = list2.next
            inter_node = inter_node.next

        if list1:
            inter_node.next = list1
        elif list2:
            inter_node.next = list2
        
        return head_node.next