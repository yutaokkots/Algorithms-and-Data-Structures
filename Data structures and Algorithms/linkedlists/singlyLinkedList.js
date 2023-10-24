/* 
Design a Singly Linked List class.

Your LinkedList class should support the following operations:

LinkedList() will initialize an empty linked list.
int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
void insertHead(int val) will insert a node with val at the head of the list.
void insertTail(int val) will insert a node with val at the tail of the list.
int remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
Example 1:

Input: 
["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

Output:
[null, null, null, true, [0, 2]]
Example 2:

Input:
["insertHead", 1, "insertHead", 2, "get", 5]

Output:
[null, null, -1]
Note:

The index int i provided to get(int i) and remove(int i) is guranteed to be greater than or equal to 0.
*/


class ListNode{
    constructor(val=0, next=null) {
        this.val = val;
        this.next = next;
    }
}
class LinkedList {
    constructor() {
        this.head = new ListNode(-1);
        this.tail = this.head;
    }

    get(index) {
        let counter = -1;
        let node = this.head;
        while (node) {
            if (counter === index) return node.val;
            node = node.next;
            counter ++;
        }
        return -1;
    }

    insertHead(val) {
        let newNode = new ListNode(val);
        let node = this.head
        let temp = node.next;
        node.next = newNode;
        newNode.next = temp;
        if (temp == null) this.tail = newNode;
    }

    insertTail(val) {
        let newNode = new ListNode(val);
        this.tail.next = newNode;
        this.tail = this.tail.next
    }

    remove(index) {
        let node = this.head
        let prev = this.head
        let counter = -1
        while (node){
            if (counter == index) break;
            prev = node
            node = node.next;
            counter ++;
        }
        if (index > counter || !node) return false;
        if (node.next){
            prev.next = node.next
        } else {
            prev.next = null;
            this.tail = prev
        }
        return true
    }

    getValues() {
        let result = []
        let node = this.head.next
        while (node){
            result.push(node.val)
            node = node.next
        }
        console.log(result)
        return result
    }
}


const ll = new LinkedList()

ll.insertHead(1)
ll.getValues()
ll.insertHead(2)
ll.getValues()
ll.insertTail(3)
ll.getValues()
ll.insertTail(4)
ll.getValues()
ll.insertHead(5)
ll.getValues()
ll.get(0)
ll.getValues()
ll.get(2)
ll.getValues()
ll.get(4)
ll.getValues()
ll.remove(2)
ll.getValues()
ll.remove(0)
ll.getValues()
ll.insertHead(6)
ll.getValues()
ll.insertTail(7)
ll.getValues()
ll.getValues()
ll.getValues()
ll.get(5)
ll.getValues()
