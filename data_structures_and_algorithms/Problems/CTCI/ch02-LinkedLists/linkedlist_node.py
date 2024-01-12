from typing import List

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LLCreator:
    def __init__(self, ll_list:List):
        self.head = self.create_linked_list(ll_list)


    def create_linked_list(self, ll_list:List):
        self.head = Node(val=ll_list[0])
        for n in range(1, len(ll_list)):
            self.add(ll_list[n])
        return self.head
        
    def add(self, n:int):
        end = Node(val=n)
        node = self.head
        while node.next != None:
            
            node = node.next
        node.next = end

    def read_ll(self):
        output = []
        head = self.head
        while head.next != None:
            output.append(head.val)
            head = head.next
        output.append(head.val)
        print(*output, sep=" -> ")
