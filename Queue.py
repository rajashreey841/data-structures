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
    def __init__(slef):
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