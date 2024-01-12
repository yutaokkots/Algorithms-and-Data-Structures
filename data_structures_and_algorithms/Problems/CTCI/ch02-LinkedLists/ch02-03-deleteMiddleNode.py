# Delete Middle Node
# Implement an algorithm to delete a node in the middle
# (i.e. any node but the first and last node, not necessarily the exact middle)
# of a singly linked list,
# given only access to that node. 
from linkedlist import Node


class Solution:
    def deleteMiddleNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


def create_linked_list(ll_list:list):
    head = Node(ll_list[0])
    for n in range(1, len(ll_list)):
        head.add(ll_list[n])
    return head

def returnMiddleNode(head, index):
    counter = 0
    while head.next:
        if counter == index:
            return head
        counter += 1
        head = head.next
    return head

def readlinkedlist(head):
    linkedList = []
    while head.next:
        linkedList.append(head.val)
        head = head.next
    linkedList.append(head.val)
    return linkedList[:]

questions = {
    "q1" : [[5, 2, 3, 24, 12, 14, 7, 11], 2],
    "q2" : [[8, 9, 7, 11, 5, 12, 4, 10, 66, 1, 32, 3], 6],
    "q3" : [[11, 5, 42, 15, 122, 66, 1, 32, 34, 10, 90, 201], 7]
}

for k, v in questions.items():
    head = create_linked_list(v[0])
    before = readlinkedlist(head)
    middle_node = returnMiddleNode(head, v[1])
    sol = Solution()
    sol.deleteMiddleNode(middle_node)
    print(f"The linked list \n before: {before}\n  after: {readlinkedlist(head)} \ncounter: {v[1]}\n\n")
