# Name: Josue Bustamante
# OSU Email: bustamjo@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 5/6/2024
# Description: A Singly Linked List data structure implementation with methods
#              to insert nodes at the front, back, and specified index of the list.
#              Additional methods include the capability to remove a node at a
#              specified index as well as that containing a specific value.
#              Finally, this code also holds methods to find a specific value and
#              count the instances of a value in a list, as well as to splice the
#              original list into a subset of that list.


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Takes a value as a parameter and inserts a node containing
        that value at the front of a linked list.
        """

        # CHECKS if linked list is empty
        if self.is_empty() is True:
            self._head.next = SLNode(value)
            return

        # INSERTS new node at head and shifts linked list
        old_node = self._head.next
        self._head.next = SLNode(value, old_node)

    def insert_back(self, value: object) -> None:
        """
        Takes a value as a parameter and inserts a node containing
        that value at the back of a linked list.
        """

        # CHECKS if linked list is empty
        if self.is_empty() is True:
            self._head.next = SLNode(value)
            return

        target = self._head.next

        # ITERATES to end of linked list
        for val in range(self.length()):
            if target.next is None:
                target.next = SLNode(value)

            target = target.next

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Takes an index and value as parameters and inserts a node
        containing that value at the index specified.
        """
        # CHECKS if index is invalid
        if index > self.length() or index < 0:
            raise SLLException

        # CHECKS if linked list is empty
        if self.is_empty() is True:
            self._head.next = SLNode(value)
            return

        # CHECKS if node will be inserted at front of linked list
        elif index == 0:
            next_node = self._head.next
            self._head.next = SLNode(value, next_node)

        target = self._head.next

        # ITERATES through list to target index
        for val in range(index):
            if val != index - 1:
                target = target.next
            else:
                target.next = SLNode(value, target.next)

    def remove_at_index(self, index: int) -> None:
        """
        Takes an index and value as parameters and removes a node
        at the index specified.
        """

        # CHECKS if index is invalid
        if index >= self.length() or index < 0:
            raise SLLException

        # CHECKS if linked list is empty
        if self.is_empty() is True:
            raise SLLException

        target = self._head.next
        next_node = target.next

        # CHECKS if front node is to be removed
        if index == 0:
            self._head.next = next_node
            return

        # ITERATES through list to reach index specified
        for val in range(index):
            if val != index - 1:
                target = target.next
            else:
                next_node = target.next
                target.next = next_node.next

    def remove(self, value: object) -> bool:
        """
        Takes a value as a parameter and removes the first instance of
        a node with containing that value, returning True if the
        procedure was successful and False otherwise.
        """

        # CHECKS if value is invalid
        if value is None:
            return False

        # CHECKS if linked list is empty
        if self.length() == 0:
            return False

        target = self._head.next

        # ITERATES through list to find value and remove if found
        for index in range(self.length()):

            if target.value == value:
                self.remove_at_index(index)
                return True

            elif target.value != value and index == self.length() - 1:
                return False

            else:
                target = target.next

    def count(self, value: object) -> int:
        """
        Takes a value as a parameter and returns a count of how many
        instances that value appears in the linked list.
        """

        # CHECKS if linked list is empty
        if self.length() == 0:
            return 0

        target = self._head.next
        count = 0

        # ITERATES through list and increments count for found value
        for index in range(self.length() + 1):
            if index == self.length():
                return count
            elif target.value == value:
                count += 1
                target = target.next
            else:
                target = target.next

    def find(self, value: object) -> bool:
        """
        Takes a value as a parameter and returns True if that value is
        found in the linked list, returning False otherwise.
        """

        # CHECKS if value is provided
        if value is None:
            return False

        # CHECKS if linked list is empty
        if self.length() == 0:
            return False

        target = self._head.next

        # ITERATES through list to find value and returns boolean value
        for index in range(self.length() + 1):

            if index == self.length():
                return False

            elif target.value == value:
                return True

            elif target.value != value:
                target = target.next

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Takes an index and size as parameters and returns a new linked
        list of the size specified containing a subset of the original
        linked list with the value starting from the index provided.
        """

        # CHECKS if size is valid
        if size < 0 or start_index + size > self.length():
            raise SLLException

        # CHECKS if start index is valid
        if start_index < 0 or start_index >= self.length():
            raise SLLException

        new_ll = LinkedList(None)
        target = self._head.next

        # ITERATES through original list to reach starting index
        for index in range(self.length() + 1):
            if index < start_index:
                target = target.next

        # ADDS values from original list to new linked list
        for val in range(size):
            if val != size:
                new_ll.insert_back(target.value)
                target = target.next

        return new_ll


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
