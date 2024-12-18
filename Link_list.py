'''

A linked list is a linear data structure where each element (called a node) contains:

Data: The value stored in the node.
Pointer: A reference to the next node in the sequence.

There are three main types of linked lists:

Singly Linked List: Each node points to the next node.
Doubly Linked List: Each node points to both the next and previous nodes.
Circular Linked List: The last node points back to the first node.
'''
# Structure of node:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None  # pointer to next node

# Structure of singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # pointer to the first node

# At the Beginning:
def insert_at_beginning(self,data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

# Insert at the end
def insert_at_end(self,data):
    new_node = Node(data)
    if self.head is None:
        self.head =  new_node
        return
    temp = self.head
    while temp.next:
        temp = temp.next
    temp.next = new_node

# Insert at specific position
def insert_at_position(self,data,position):
    if position == 0:
        self.insert_at_beinning(data)
        return
    new_node = None(data)
    temp = self.head
    for _ in range(position-1):
        if temp is None:
            raise IndexError("Position out of range")
        temp = temp.next
    new_node.next = temp.next
    temp.next = new_node
    

        