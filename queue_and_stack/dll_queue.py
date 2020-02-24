import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # It allows for dynamic sizing/an array has to know its size before it is created or reallocate memory as it grows.
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.storage.head is None:
            return None
        else:
            return self.storage.remove_from_head()

    def len(self):
        return self.storage.length

# A queue is a collection of objects that follows First In First Out (FIFO) for inserting and deleting. It adds objects at the end and only allows for access and deletion from the first (Head) location.
