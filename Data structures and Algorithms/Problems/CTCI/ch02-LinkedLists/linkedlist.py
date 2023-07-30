class Node:
    def __init__(self, d:int):
        self.head = self
        self.val = d
        self.next = None

    def add(self, d:int):
        end = Node(d)
        n = self
        while n.next != None:
            n = n.next
        n.next = end
    
    # add head node, and the n'th number of the linked list to make into a cycle. 
    def make_cyclic(self, n:int):
        node = self
        anchor = None
        counter = 0
        while node.next != None:
            if counter == n:
                anchor = node
            node = node.next    
            counter += 1
            if node.next == None:
                node.next = anchor
                break

    def read_ll(self):
        output = []
        head = self
        while head.next:
            output.append(head.val)
            head = head.next
        output.append(head.val)
        return output
    

    # head = Node(5)
    # head.add(2)
    # head.add(3)
    # head.add(24)
    # head.add(12)
    # head.add(14)
    # head.add(7)
    # head.make_cyclic(4)


    # def delete(self, head, d:int):
    #     node = head
    #     if node.val == d:
    #         return head.next

    #     while node.next != None:
    #         if node.next == node.next.next:
    #             return head
    #         node = node.next
    #     return head
    