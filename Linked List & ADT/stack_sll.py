# Name: Josue Bustamante
# OSU Email: bustamjo@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 5/6/2024
# Description: A Stack ADT class implementation utilizing a singly linked list
#              containing methods for pushing, popping, and determining values
#              from the top of the stack.


from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
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
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Takes a value as a parameter ands a node containing that value to
        the top of the stack.
        """

        # CHECKS if stack is empty
        if self.is_empty() is True:
            self._head = SLNode(value)
            return

        # ADDS node to the top of the stack
        next_node = self._head
        self._head = SLNode(value)
        self._head.next = next_node

    def pop(self) -> object:
        """
        Removes the node at the top of the stack and returns
        the value it contains.
        """

        # CHECKS if stack is empty
        if self.is_empty() is True:
            raise StackException

        # REMOVES top of stack and returns the contained value
        value = self._head.value
        self._head = self._head.next
        return value

    def top(self) -> object:
        """
        Returns the value contained by the node at the top of the stack
        """

        # CHECKS if stack is empty
        if self.is_empty() is True:
            raise StackException

        return self._head.value

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
