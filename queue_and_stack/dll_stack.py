
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # It allows for dynamic sizing/an array has to know its size before it is created or reallocate memory as it grows.
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        if self.storage.head is None:
            return None
        else:
            return self.storage.remove_from_head()


    def len(self):
        return self.storage.length

# A stack is a collection of objects that follows the Last In First Out (LIFO) for inserting and deleting objects. So users can only access the most recently inserted object (the Head).
