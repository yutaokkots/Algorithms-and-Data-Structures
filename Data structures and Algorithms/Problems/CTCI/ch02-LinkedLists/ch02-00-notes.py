# Runner technique

# iterate through the linked list with two pointers simultaneously. 

# Example: cycle through linked list. 

from linkedlist import Node

## creating a cyclic linked list:
head = Node(5)
head.add(2)
head.add(3)
head.add(24)    # <--------|
head.add(12)            #  |
head.add(14)            #  |
head.add(7)             #  |
head.make_cyclic(3)     # makes the end link to position 3 of linked list from head.  (24)

## creating an acylic linked list:
head2 = Node(8)
head2.add(5)
head2.add(4)
head2.add(13)   
head2.add(11)            
head2.add(17)           
head2.add(7)             




## Use the 'Runner Technique' to check for a cyclic linked list. 


class Solution:
    def check_cyclic(self, head:Node) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

sol = Solution()
answer1 = sol.check_cyclic(head)
answer2 = sol.check_cyclic(head2)
print(f"This is a cyclic linked list: {answer1}")
print(f"This is a cyclic linked list: {answer2}")