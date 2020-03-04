'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''

#create a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    #insert a new node at the beginning of the linkedlist
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverseList(self):
        prev = None
        curr = self.head
        
        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev

    def printList(self,head):
        temp = head
        while(temp):
            print(temp.data, end= ' ')
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(6)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(9)
    llist.push(10)
    head = llist.reverseList()
    print(llist.printList(head))
    
        
