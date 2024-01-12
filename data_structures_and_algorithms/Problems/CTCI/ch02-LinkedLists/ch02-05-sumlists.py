from linkedlist_node import Node, LLCreator
# You have two numbers represented by a linked list, where
# each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list/
# write a function that adds the two numbers and returns the summation as a linked list/ 

# example
# input: (7 -> 1-> 6 ) + (5 -> 9 -> 2) = 617 + 295
# output: 2 -> 1 -> 9 (i.e. 912)

# write a second function in forward order
# example 2
# input: (6 -> 1 -> 7) + (2 -> 9 -> 5) = 617 + 295
# output: 9 -> 1-> 2; 912

class Solution():
    def sum_lists_backwards(self, head1, head2):
        lst = []
        remainder = 0
# 
        # [7,1,6,9] -> 9617
        # [5,9,2]   ->  295  -> 9912

        def add_values(h1=0, h2=0, r=0):
            summation = h1 + h2 + r
            if summation > 19:
                summation -= 20
                r = 2
            elif summation > 9:
                summation -= 10
                r = 1
            else: 
                r = 0
            lst.append(summation)
            return r

        remainder = add_values(head1.val, head2.val, remainder)
        while head1.next != None and head2.next != None:
            head1 = head1.next
            head2 = head2.next
            remainder = add_values(head1.val, head2.val, remainder)

        while head1.next != None or head2.next != None:
            if head1.next != None:
                head1 = head1.next
                remainder = add_values(head1.val, 0, remainder)           
            elif head2.next != None:
                head2 = head2.next
                remainder = add_values(0, head2.val, remainder)

        add_values(0,0, remainder)

        prev = None

        for i, n in enumerate(lst):
            if i == len(lst) -1 and n == 0:
                continue
            elif i == 0:
                node = head = Node(n)
                prev = node
            else:
                node = Node(n)
                prev.next = node
                prev = node
            
        return head        

    def sum_lists_forwards(self, head1, head2):
        pass

def read_ll(head):
    output = []
    while head.next:
        output.append(head.val)
        head = head.next
    output.append(head.val)
    return output

ll_1 = LLCreator([9,9,9,5])
ll_2 = LLCreator([2, 6 ])

head1 = ll_1.head
head2 = ll_2.head

sol = Solution()
answer = sol.sum_lists_backwards(head1, head2)
print(read_ll(answer))




