# Name: Josue Bustamante
# OSU Email: bustamjo@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date:4/29/2024
# Description: Methods for implementing a DynamicArray class with features
#              including resizing, appending, inserting, removing, slicing,
#              mapping, filtering, and reducing.


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def get_size(self):
        return self._size

    def resize(self, new_capacity: int) -> None:
        """
        Takes an integer as a parameter and resizes the array to the new
        capacity if it is not smaller than the current size.
        """
        if new_capacity <= 0:
            return None

        if new_capacity < self._size:
            return None

        old_arr = self._data
        self._data = StaticArray(new_capacity)
        self._capacity = new_capacity

        # SETS elements to fresh larger array
        if new_capacity > old_arr.length():
            for index in range(old_arr.length()):
                self._data.set(index, old_arr.get(index))
        else:
            # SETS elements to fresh smaller array
            for index in range(new_capacity):
                self._data.set(index, old_arr.get(index))



    def append(self, value: object) -> None:
        """
        Takes a value as a parameter and adds it to the end of the
        elements in the list.
        """
        # DOUBLES array capacity if reached
        if self._size >= self._capacity:
            self.resize(self._capacity * 2)

        # APPENDS value
        self._data[self._size] = value
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Takes an index and a value as parameters and inserts the value
        at the index specified.
        """
        # DOUBLES capacity if reached
        if self._size >= self._capacity:
            self.resize(self._capacity * 2)

        # RAISES exception if index is invalid
        if index > self._size or index < 0:
            raise DynamicArrayException

        # MOVES elements to allow for new value
        count = self._size - 1
        for val in range(index, self.length()):
            self._data.set(count + 1, self._data.get(count))
            count -= 1

        # INSERTS value into place
        self._data.set(index, value)
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
        Takes an index as a parameter and removes the element of the
        array found at the index specified.
        """
        # RAISES exception if index is invalid
        if index > self._size - 1 or index < 0:
            raise DynamicArrayException

        # RESIZES array if under 25% capacity
        if self._size < self._capacity / 4:
            if self._capacity <= 10:
                pass
            if self._capacity > 10:
                if self._size >= 5:
                    self.resize(self._size * 2)
                else:
                    self.resize(10)

        # MOVES elements to occupy the empty space
        for val in range(index, self._size - 1):
            self._data[val] = self._data[val + 1]
            self._data[val + 1] = None

        self._size -= 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Takes a starting index and a size as parameters and returns
        a new array of the size specified, made from the elements
        of the original array starting from the index specified.
        """
        # RAISES exception if size is invalid
        if size < 0 or start_index + size > self._size:
            raise DynamicArrayException

        # RAISES exception if index is invalid
        if start_index < 0 or start_index >= self._size:
            raise DynamicArrayException

        new_arr = DynamicArray()

        # APPENDS elements from old array to new array
        count = 0
        for index in range(size):
            new_arr.append(self._data[start_index + count])
            count += 1
        return new_arr

    def map(self, map_func) -> "DynamicArray":
        """
        Takes a map function as a parameter and returns a dynamic array
        with elements being derived from the map function being applied
        to the elements of the original array.
        """
        # APPENDS new elements to new array
        new_arr = DynamicArray()
        for index in range(self._size):
            new_arr.append(map_func(self._data[index]))
        return new_arr

    def filter(self, filter_func) -> "DynamicArray":
        """
        Takes a filter function as a parameter and returns a new
        dynamic array with the elements filtered as specified
        from the old array.
        """
        # APPENDS filtered elements to new array
        new_arr = DynamicArray()
        for index in range(self._size):
            if filter_func(self._data[index]) is True:
                new_arr.append(self._data[index])
        return new_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Takes a reduce function and an optional initializer as
        parameters and returns the value derived from the reduce
        function
        """
        start_index = 0

        # IF array is empty
        if self._size == 0:
            return initializer

        # SETS initializer to first element
        if initializer is None:
            initializer = self._data[0]
            start_index = 1

        # LOOPS reduce function
        for index in range(start_index, self._size):
            result = reduce_func(initializer, self._data[index])
            initializer = result

        return initializer


def chunk(arr: DynamicArray) -> "DynamicArray":
    """
    Takes a dynamic array as a parameter and returns a new dynamic array
    holding arrays of the contents of the original array in ascending order.
    """
    master_arr = DynamicArray()
    count = 0
    start = 0
    for index in range(arr.length()):
        count += 1

        # IF end of array is reached
        if index == arr.length() - 1:
            new = arr.slice(start, count)
            master_arr.append(new)
            return master_arr

        # CREATES new array if next element is not in ascending order
        if arr[index + 1] < arr[index]:
            new = arr.slice(start, count)
            master_arr.append(new)
            start = index + 1
            count = 0
    return master_arr


def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    Takes a dynamic array as a parameter and returns a tuple containing
    a dynamic array of the mode elements with the most instances in the
    array as well as the total count of instances.
    """

    new_index = 0
    count_1 = 0
    count_2 = 0
    new_arr = DynamicArray()

    # IF array has only one value
    if arr.length() == 1:
        new_arr.append(arr[0])
        return (new_arr, 1)

    for index in range(arr.length()):

        # FIRST VALUE
        if index == 0:
            count_1 += 1
            new_arr.append(arr[index])

        # IF element is a repeat instance
        elif arr[index] == new_arr[new_index]:

            # IF only one element is being counted
            if count_2 == 0:
                count_1 += 1
            # IF a second element is being counted
            elif count_2 != 0:
                count_2 += 1
            # IF end of array is reached
            if index == arr.length() - 1 and count_2 != 0:
                if count_2 < count_1:
                    new_arr.remove_at_index(new_index)

        # IF elements is not a repeat instance
        elif arr[index] != new_arr[new_index]:

            # IF end of array is reached
            if index == arr.length() - 1:
                # IF highest count is 1
                if count_1 == 1:
                    new_arr.append(arr[index])
                # IF only one element is being counted
                elif count_2 == 0:
                    return (new_arr, count_1)
                # IF second element has more instances than the first
                if count_2 < count_1 and count_2 != 0:
                    new_arr.remove_at_index(new_index)

            # IF a second element has not been counted
            elif count_2 == 0:
                new_arr.append(arr[index])
                new_index += 1
                count_2 = 1

            # CHECKS if element can be discarded
            elif count_1 > count_2:
                new_arr.remove_at_index(new_index)
                new_arr.append(arr[index])
                count_2 = 1

            else:
                new_arr.append(arr[index])
                new_index += 1
                count_2 = 1

        # CHECKS if entire array should be replaced
        if count_2 > count_1:
            new_arr = DynamicArray()
            new_arr.append(arr[index])
            count_1 = count_2
            count_2 = 0
            new_index = 0

    # FINALIZES new array
    old_arr = new_arr
    new_arr = DynamicArray()
    for index in range(old_arr.length()):
        new_arr.append(old_arr[index])
    return (new_arr, count_1)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    def print_chunked_da(arr: DynamicArray):
        if len(str(arr)) <= 100:
            print(arr)
        else:
            print(f"DYN_ARR Size/Cap: {arr.length()}/{arr.get_capacity()}")
            print('[\n' + ',\n'.join(f'\t{chunk}' for chunk in arr) + '\n]')

    print("\n# chunk example 1")
    test_cases = [
        [10, 20, 30, 30, 5, 10, 1, 2, 3, 4],
        ['App', 'Async', 'Cloud', 'Data', 'Deploy',
         'C', 'Java', 'Python', 'Git', 'GitHub',
         'Class', 'Method', 'Heap']
    ]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# chunk example 2")
    test_cases = [[], [261], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
