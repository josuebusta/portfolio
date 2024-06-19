# Name: Josue Bustamante
# OSU Email: bustamjo@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date:5/28/2024
# Description: Methods for implementing a minimum binary heap class with features
#              including adding an element with a specified priority value,
#              and removing the element with the lowest priority value.
#              Additional methods return the element with the lowest
#              priority value, whether the heap is empty, the size of the heap,
#              and a clear heap. Finally, a method to build a heap and a method to
#              sort the heap in non-ascending order are included.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MinHeap with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MinHeap content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return "HEAP " + str(heap_data)

    def add(self, node: object) -> None:
        """
        Takes an object as a parameter and adds it to the MinHeap
        while maintaining priority order.
        """

        # SET next open spot
        nop = self.size()

        # IF heap is empty
        if self.size() == 0:
            self._heap.append(node)
            return

        # ADDS element to heap
        self._heap.insert_at_index(nop, node)

        # COMPUTES inserted element's parent index
        nop_par = (nop - 1) // 2

        # COMPARES values of inserted element and parent element
        for val in range(self.size() - 1):
            if self._heap[nop_par] > self._heap[nop]:

                # SWAPS elements if parent element is greater
                temp = self._heap[nop_par]
                self._heap[nop_par] = node
                self._heap[nop] = temp
                nop = nop_par
                nop_par = (nop - 1) // 2

            # ENDS if parent index is invalid
            if nop_par < 0:
                return


    def is_empty(self) -> bool:
        """
        Returns true if heap is empty, returning false otherwise.
        """
        if self.size() == 0:
            return True
        elif self.size() != 0:
            return False

    def get_min(self) -> object:
        """
        Returns the element of the heap with the lowest priority value.
        """
        # CHECKS if heap is empty
        if self.size() == 0:
            raise MinHeapException

        return self._heap[0]

    def remove_min(self) -> object:
        """
        Removes the element with the lowest priority value from the heap
        while maintaining heap priority.
        """

        # CHECKS if heap is empty
        if self.size() == 0:
            raise MinHeapException

        target = self.size() - 1
        par = 0
        val = self._heap[par]

        # REPLACES first element with the last element
        self._heap[par] = self._heap[target]
        self._heap.remove_at_index(target)

        # CHECKS if heap has only one element
        if self.size() == 1:
            return val

        # COMPARES target element with children
        # PERCOLATES down if higher priority value
        _percolate_down(self._heap, par)
        return val

    def build_heap(self, da: DynamicArray) -> None:
        """
        Takes a dynamic array object as a parameter and builds
        a heap out of the current elements of the array.
        """

        # COMPUTES first non-leaf element of heap
        target = (da.get_size() - 1) // 2

        # ADDS elements of dynamic array to cleared heap
        self.clear()
        for index in range(da.get_size()):
            self._heap.append(da[index])

        # PERCOLATES non-leaf elements to confirm subtree heap property
        for val in range(target + 1):
            _percolate_down(self._heap, target)
            target -= 1



    def size(self) -> int:
        """
        Returns heap size.
        """
        return self._heap.get_size()

    def clear(self) -> None:
        """
        Clears elements from heap.
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    Takes a dynamic array object as a parameter and sorts
    the elements in non-ascending order with the Heapsort
    algorithm.
    """

    # COMPUTES first non-leaf element of heap
    target = (da.get_size() - 1) // 2

    # PERCOLATES non-leaf elements to confirm subtree heap property
    for val in range(target + 1):
        _percolate_down(da, target)
        target -= 1

    # SETS last element of array
    target = da.get_size() - 1

    for val in range(da.get_size()):
        # SWAPS first and last element
        parent = 0
        temp = da[parent]
        da[parent] = da[target]
        da[target] = temp

        # COMPUTES child indices
        child_1 = 2 * parent + 1
        child_2 = 2 * parent + 2

        # IF both child node indices are in range
        while child_1 < target and child_2 < target:

            # SWAPS parent with first child node if it is the minimum child
            if da[child_1] <= da[child_2] and da[parent] >= da[child_1]:
                temp = da[child_1]
                da[child_1] = da[parent]
                da[parent] = temp
                parent = child_1
                child_1 = 2 * parent + 1
                child_2 = 2 * parent + 2

            # SWAPS parent with second child node if it is the minimum child
            elif da[child_1] > da[child_2] and da[parent] >= da[child_2]:
                temp = da[child_2]
                da[child_2] = da[parent]
                da[parent] = temp
                parent = child_2
                child_1 = 2 * parent + 1
                child_2 = 2 * parent + 2

            # RETURNS when process is done
            else:
                break

        # CHECKS if parent has only one child node
        if child_1 < target and da[parent] >= da[child_1]:
            temp = da[child_1]
            da[child_1] = da[parent]
            da[parent] = temp

        target -= 1


# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    Takes a dynamic array object and a parent node index as
    parameters, comparing and / or swapping the parent with its
    minimum child to navigate to the appropriate location in the heap.
    """

    # COMPUTES child indices
    child_1 = 2 * parent + 1
    child_2 = 2 * parent + 2

    # CHECKS if heap has only two elements in the wrong order
    if da.get_size() == 2 and da[0] > da[1]:
        temp = da[child_1]
        da[child_1] = da[parent]
        da[parent] = temp
        return

    # IF both child node indices are in range
    while child_1 < da.get_size() and child_2 < da.get_size():

        # SWAPS parent with first child node if it is the minimum child
        if da[child_1] <= da[child_2] and da[parent] >= da[child_1]:
            temp = da[child_1]
            da[child_1] = da[parent]
            da[parent] = temp
            parent = child_1
            child_1 = 2 * parent + 1
            child_2 = 2 * parent + 2

        # SWAPS parent with second child node if it is the minimum child
        elif da[child_1] > da[child_2] and da[parent] >= da[child_2]:
            temp = da[child_2]
            da[child_2] = da[parent]
            da[parent] = temp
            parent = child_2
            child_1 = 2 * parent + 1
            child_2 = 2 * parent + 2

        # RETURNS when process is done
        else:
            return

    # CHECKS if parent has only one child node
    if child_1 < da.get_size() and da[parent] >= da[child_1]:
        temp = da[child_1]
        da[child_1] = da[parent]
        da[parent] = temp








# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - remove_min example 2")
    print("--------------------------")
    h = MinHeap([-12933, 8060, 15941, 53642, 20729, 15941])
    print(h, end=' ')
    print(h.remove_min())
    print(h, end=' ')

    print("\nPDF - remove_min example 3")
    print("--------------------------")
    h = MinHeap([-36934, 99890, -14132])
    print(h, end=' ')
    print(h.remove_min())
    print(h, end=' ')

    print("\nPDF - remove_min example 4")
    print("--------------------------")
    h = MinHeap([-32984, -13255, -13255, 6097, 12013, 72327])
    print(h, end=' ')
    print(h.remove_min())
    print(h, end=' ')

    print("\nPDF - remove_min example 5")
    print("--------------------------")
    h = MinHeap([-70513])
    print(h, end=' ')
    print(h.remove_min())
    print(h, end=' ')


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    h = MinHeap([53, 25, 21, 44, 66, 52, 18, 39, 97, 51, 32, 42])
    h.remove_min()
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - build_heap example 2")
    print("--------------------------")
    da = DynamicArray([32, 12, 2, 8, 16, 20, 24, 40, 4])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("\nPDF - build_heap example 3")
    print("--------------------------")
    da = DynamicArray([11490, -65845, -86941, -8057, 88853, 83158, 91106, 22973, -36372, 29715])
    h = MinHeap([-78231, -55906, -75312, 50812, -41508, 44367, 41523, 78173])
    print(h)
    h.build_heap(da)
    print(h)

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 3")
    print("------------------------")
    da = DynamicArray([-14573, 45252])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
