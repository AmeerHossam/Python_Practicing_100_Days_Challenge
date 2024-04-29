class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #NULL

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertAtBegin(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    #Adding values to the list from the last    
    def insertAtLast(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def printLL(self):
        current_node = self.head
        while current_node:
            print(f"{current_node.data}->",end='')
            current_node = current_node.next

llist = LinkedList()
llist.insertAtLast("B")
llist.insertAtLast("45")
llist.printLL()


