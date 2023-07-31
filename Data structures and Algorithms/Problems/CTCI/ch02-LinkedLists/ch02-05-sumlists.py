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

        def add_values(h1=0, h2=0, r=0):
            summation = h1 + h2 + r
            if summation > 19:
                summation -= 20
                r = 2
            elif summation > 9:
                summation -= 10
                r = 1
            lst.append(summation)
            return r

        while head1.next != None or head2.next != None:
            print(head1.val)
            print(head2.val)
            # remainder = add_values(head1.val, head2.val, remainder)
            head1 = head1.next
            head2 = head2.next
        # add_values(head1, head2, remainder)
        print(head1.val)
        print(head2.val)
        print(*lst)




    def sum_lists_forwards(self, head1, head2):
        pass


ll_1 = LLCreator([7,1,6,9])
ll_2 = LLCreator([5,9,2])

head1 = ll_1.head
head2 = ll_2.head

sol = Solution()
sol.sum_lists_backwards(head1, head2)