# Name: Josue Bustamante
# OSU Email: bustamjo@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 4/29/2024
# Description: Methods to implement a Bag class. Features include
#              adding, removing, and counting elements, clearing the array,
#              determining equality, and implementing iteration.


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Takes a value as a parameter and adds that value to
        the bag array.
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Takes a value as a parameter and returns True if it's possible
        to remove an instance of that value from teh bag array, returning
        False otherwise
        """
        result = None
        for index in range(self.size()):
            if self._da[index] == value and result is None:
                self._da.remove_at_index(index)
                return True

        return False

    def count(self, value: object) -> int:
        """
        Takes a value as a parameter and returns the amount of instances
        that value is found in the bag array.
        """
        count = 0
        for index in range(self.size()):
            if self._da[index] == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        Clears the bag array to a size of 0.
        """
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        Takes a second bag array as a parameter and returns True
        if the two bag arrays are equal in size and elements, returning
        False otherwise.
        """

        # CHECKS if bag array sizes are unequal
        if self.size() != second_bag.size():
            return False

        # CHECKS if bag array size is 0
        if self.size() == 0 and second_bag.size() == 0:
            return True

        # COUNTS instances of each element in one array and compares it to the other
        for index in range(self.size()):
            num = self._da[index]
            count_1 = self.count(num)
            count_2 = second_bag.count(num)
            if count_1 != count_2:
                return False

        return True

    def __iter__(self):
        """
        Creates iterator for loop.
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Advances iterator by moving to the next index.
        """
        try:
            value = self._da[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index = self._index + 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
