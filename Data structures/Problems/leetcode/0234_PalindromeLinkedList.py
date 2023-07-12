# Given the head of a singly linked list, return true if it is a 
# palindrome or false otherwise.
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Class for solution. 
class Solution:
    def isPalindrome(self, head: any[ListNode]) -> bool:
        stack = []
        # stack [4, 5, 6] <- 6
        # stack [] 4
        while head.next:
            stack.append(head.val)
            head = head.next
            if not head.next:
                stack.append(head.val)
        if len(stack) == 0 or len(stack) == 1:
            return True
        l = 0
        r = len(stack) - 1
        while l < r:
            if stack[l] != stack[r]:
                return False
            l += 1
            r -= 1
        return True

    def isPalindrome2(self, head: any[ListNode]) -> bool:
        while head.next:
            head = head.next
            pass

    
def create_linked_list():
    #initialize a list that stores the node information 
    node_list = []
    # create a node head
    head = ListNode(random.randint(-100, 100))
    # determine the length of the linked list
    length = random.randint(3, 16)
    for n in range(length):
        if n == 0:
            node_list.append(ListNode(head))
        else:
            value = random.randint(-100, 100)
            node = ListNode(value)
            node_list[-1].next = node
            node_list.append(node)
    return node_list[0]

def create_palindromic_linked_list():
    #initialize a list that stores node information
    node_list = []
    #create a node head
    head = ListNode(random.randint(-100,100))
    length_half = random.randint(2, 8)
    for n in range(length_half):
        if n == 0:
            node_list.append(ListNode(head))
        else:
            value = random.randint(-100,100)
            node = ListNode(value)
            node_list[-1].next = node 
            node_list.append(node)
    size = len(node_list) - 1
    for n in range(size, -1, -1):
        node = ListNode(node_list[n].val)
        if node_list[n] == node_list[-1]:
            node_list[n].next = node
            node_list.append(node)
        else:
            node_list[-1].next = node
            node_list.append(node)
    return node_list[0]

head_1 = ref_1 = create_linked_list()
head_2 = ref_2 = create_palindromic_linked_list()

def read_linked_list(head):
    while head.next:
        print(head.val)
        head = head.next

# read_linked_list(ref_1)
# read_linked_list(ref_2)

