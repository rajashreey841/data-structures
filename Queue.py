'''
Queue is a linear data structure that follows the First In, First Out(FIFO) principle,means the first element added is the first one to be removed.

Queue Operation:
1.Enqueue:Adds an element to the rear of the queue.
2.Dequeue:Removes an element from the front of the queue.
3.Peek/Front:Views the element at the front of the queue without removing it.
4.Is Empty:Checks if the queu is empty.

'''
# Implementation using a custom class

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue
    def enqueue(self,element):
        self.queue.append(element)

    # Dequeue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    # Peek
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    # is_empty
    def is_empty(self):
        return len(self.queue) == 0

    # size
    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(7)
q.enqueue(10)
print("Queue after enqueue:", q.queue)  
print("Front element:", q.peek())  
q.dequeue()
print("Queue after dequeue:", q.queue) 
print("Is queue empty?", q.is_empty())  
print("Size of queue:", q.size()) 


# Implementation using Collection(Deque)
from collections import deque

# Create a queue
queue = deque()

# Enqueue
queue.append(10)
queue.append(20)

# Dequeue
queue.popleft()

# Peek
if queue:
    print(queue[0])

# Is Empty
print(len(queue) == 0)

# Size
print(len(queue))

# Implementation using the queue module
from queue import Queue

# Create a queue
q = Queue()

# Enqueue
q.put(10)
q.put(20)

# Dequeue
print(q.get())

# Peek (not directly supported; use workaround)
if not q.empty():
    print(q.queue[0])

# Is Empty
print(q.empty())

# Size
print(q.qsize())