from linkedlist import Node

# remove duplicates
# write code to remove duplicates from an unsorted linked list
# follow-up: how would you solve this problem if a temporary buffer is not allowed?

ll_1 = [5, 2, 3, 24, 12, 14, 7, 11]
ll_2 = [8, 9, 1, 11, 9, 12, 4, 10, 8, 1, 1, 3]

def create_linked_list(ll_list:list) -> Node:
    head = Node(ll_list[0])
    for n in range(1, len(ll_list)):
        head.add(ll_list[n])
    return head

head1 = create_linked_list(ll_1)
head2 = create_linked_list(ll_2)

# head1 = Node(5)
# head1.add(2)
# head1.add(3)
# head1.add(24)    
# head1.add(12)    
# head1.add(14)    
# head1.add(7)     
# head1.add(11)     

# head2 = Node(8)
# head2.add(9 )
# head2.add(1 )
# head2.add(11)    
# head2.add(9 )    
# head2.add(12)    
# head2.add(4 )     
# head2.add(10)    

class Solution():
    def remove_duplicates(self, head:Node):
        memo = []
        prev = None
        while head.next:
            if head.val not in memo:
                memo.append(head.val)
                prev = head
            else:
                prev.next = head.next
            
            head = head.next

result = head1.read_ll()
result2 = head2.read_ll()
print(result)
print(result2)

head3 = create_linked_list(ll_1)
head4 = create_linked_list(ll_2)

sol = Solution()
sol.remove_duplicates(head3)
sol.remove_duplicates(head4)

print(head3.read_ll())
print(head4.read_ll())
