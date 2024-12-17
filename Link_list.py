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
        