# Palindrome
# implement a functino to check if a linked list is a palindrome
from linkedlist_node import Node, LLCreator

l_1 = [1, 2, 3, 3, 2, 1]
l_2 = [2, 3, 3, 4, 5, 4, 3, 3, 2]
l_3 = ["A", "B", "B", "A"]
l_4 = ["A", "B", "B", "d"]

ll1 = LLCreator(l_1)
ll2 = LLCreator(l_2)
ll3 = LLCreator(l_3)
ll4 = LLCreator(l_4)

ll_1 = ll1.head
ll_2 = ll2.head
ll_3 = ll3.head
ll_4 = ll4.head

class Solution:
    def checkPalindrome(self, head:Node) -> bool:
        record = []
        while head.next:
            record.append(head.val)
            head = head.next
            if head.next == None:
                record.append(head.val)
        print(record)
        return record == record[::-1]
    
    # The following approach uses the slow and fast pointers
    # the slow pointer proceeds at half of the rate as the fast pointer.
    # when the fast pointer reaches the end, the slow pointer is in the middle. 
    def checkPalindromeSlowFast(self, head:Node) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head
        stack = []
        while fast != None and fast.next != None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast != None:
            slow = slow.next

        while slow != None:
            popped_val = stack.pop()
            if slow.val != popped_val:
                return False
            slow = slow.next
        return True
    
sol = Solution()

# print(sol.checkPalindrome(ll_1))
# print(sol.checkPalindrome(ll_2))
# print(sol.checkPalindrome(ll_3))

print(sol.checkPalindromeSlowFast(ll_1))
print(sol.checkPalindromeSlowFast(ll_2))
print(sol.checkPalindromeSlowFast(ll_3))
print(sol.checkPalindromeSlowFast(ll_4))