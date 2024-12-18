'''
A stack is a linear data structure that follows that Last In, First Out(LIFO) principle,means the last element added
is the first one be removed.

Stack operation:
1.Push: Add an item to top of the stack
2.Pop: Removes the item from the top of the stack
3.Peek/Top: Views the item at the top of the stack without removing it.
4.Is EMpty: Checks if the stack is empty.
'''
# All operation using List(Built in python) and Custom class


class Stack:
    def __init__(self):
        self.stack = []
    
    # Push
    def push(self,element):
        self.stack.append(element)

    # Pop
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("stack is empty")
    '''
    or
    if stack:
        stack.pop()
    else:
        print("stack is empty")
    '''

    # Peek
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
    '''
    or
    if stack:
        print(stack[-1])
    '''

    # Is Empty
    def is_empty(self):
        return len(self.stack)==0
    '''
    or
    if not stack:
        print("stack is empty")
    '''

    # Size
    def size(self):
        return len(self.stack)

s = Stack()
s.push(7)
s.push(14)
print("Stack after pushing",s.stack)
print("Top element: ",s.peek())
s.pop()
print("Pop element: ",s.stack)
print("Peek :",s.peek())
print("Is stack empty:", s.is_empty())
print("size of stack:",s.size())

# Implementing using Collections(Deque)
from collections import deque

stack = deque()

# Push
print("-----Collection----")
stack.append(4)
stack.append(8)
stack.append(12)

# Pop
print(stack.pop())

# Peek
if stack:
    print(stack[-1])

# Is Empty
print(len(stack)==0)

# Size
print(len(stack))
