# implement an algorithm to find the kth to last element of a singly linked list
from linkedlist import Node

class Solution:
    def return_kth(self, head, k:int) -> int:
        stack = []
        while head.next:
            stack.append(head.val)
            head = head.next
        stack.append(head.val)
        return(stack[-k])


def create_linked_list(ll_list:list):
    head = Node(ll_list[0])
    for n in range(1, len(ll_list)):
        head.add(ll_list[n])
    return head

questions = {
    "q1" : [[5, 2, 3, 24, 12, 14, 7, 11], 2],
    "q2" : [[8, 9, 7, 11, 5, 12, 4, 10, 66, 1, 32, 3], 6],
    "q3" : [[11, 5, 42, 15, 122, 66, 1, 32, 34, 10, 90, 201], 10]
}

for k, v in questions.items():
    head = create_linked_list(v[0])
    sol = Solution()
    answer = sol.return_kth(head, v[1])
    print(f"for linked list: {v[0]}, \nthe {v[1]}th from the last index is: {answer}\n")
