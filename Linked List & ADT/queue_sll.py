# Name: Josue Bustamante
# OSU Email: bustamjo@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 5/6/2024
# Description: A Queue ADT class implementation utilizing a singly linked list
#              and containing methods to enqueue and dequeue elements as well as
#              returning the top element.


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Takes a value as a parameter and adds a node containing that value
        to the end of the queue.
        """

        # CHECKS if queue is empty
        if self.is_empty() is True:
            self._head = SLNode(value)
            self._tail = self._head
            return

        self._tail.next = SLNode(value)
        self._tail = self._tail.next

    def dequeue(self) -> object:
        """
        Removes the node at the front of a queue and returns its value.
        """

        # CHECKS if queue is empty
        if self.size() == 0:
            raise QueueException

        value = self._head.value
        self._head = self._head.next
        return value

    def front(self) -> object:
        """
        Returns the value contained by the node at the front of the queue.
        """
        # CHECKS if queue is empty
        if self.size() == 0:
            raise QueueException

        value = self._head.value
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
