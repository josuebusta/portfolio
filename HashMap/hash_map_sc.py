# Name: Josue Bustamante
# OSU Email: bustamjo@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: 6/6/24
# Description: An implementation of an optimized HashMap class with chaining for collision resolution.
#              Includes methods to insert a key and value pair into the Hashmap or remove them, resize or
#              clear the map, and search for keys. Other methods have  capabilities to return the load factor,
#              the amount of empty buckets, and an array with the  keys and values.
#              A final function returns the mode of a Dynamic Array using a HashMap.

from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Takes a key and value pair as parameters and inserts the values
        into the hash map.
        """
        # CHECKS if table needs resizing
        if self.table_load() >= 1:
            new_cap = self._capacity * 2
            self.resize_table(new_cap)

        # CHECKS if key is already in hash map
        bucket = self.compute_bucket(key)
        node = bucket.contains(key)

        # IF key already exists in map
        if node is not None:
            node.value = value
            return

        # IF key is not in map
        bucket.insert(key, value)
        self._size += 1

    def resize_table(self, new_capacity: int) -> None:
        """
        Takes a new capacity as a parameter and adjusts the table's
        capacity and elements accordingly.
        """

        # CHECKS if new capacity is valid
        if new_capacity < 1:
            return

        # CHECKS if new capacity is a prime number
        if self._is_prime(new_capacity) is False:
            new_capacity = self._next_prime(new_capacity)

        # STORES key and value pairs
        kav = self.get_keys_and_values()

        # CLEARS hash map
        self._buckets = DynamicArray()
        self._capacity = new_capacity
        self._size = 0
        for val in range(self._capacity):
            self._buckets.append(LinkedList())

        # ADDS key / value pairs with new hash
        for index in range(kav.length()):
            val_1 = kav[index][0]
            val_2 = kav[index][1]
            self.put(val_1, val_2)

    def table_load(self) -> float:
        """
        Returns the hash table load factor.
        """
        result = self._size / self._capacity
        return result

    def empty_buckets(self) -> int:
        """
        Returns the amount of empty buckets in the hash map.
        """

        # ITERATES through hash map to return count
        count = 0
        for index in range(self._capacity):
            if self._buckets[index].length() == 0:
                count += 1

        return count

    def get(self, key: str):
        """
        Takes a key as a value and returns the value
        of that key if found in the hash map.
        """

        # CHECKS if key is in map
        bucket = self.compute_bucket(key)
        result = bucket.contains(key)

        # IF successful
        if result is not None:
            return result.value

    def contains_key(self, key: str) -> bool:
        """
        Takes a key as a parameter and returns True
        if it is found in the hash map, returning
        False otherwise.
        """

        # CHECKS if hash map is empty
        if self._size == 0:
            return False

        # CHECKS if key is in map
        bucket = self.compute_bucket(key)
        if bucket.contains(key) is not None:
            return True

        return False

    def remove(self, key: str) -> None:
        """
        Takes a key as a parameter and removes the key and value
        pair from hash map if the key is found.
        """
        # CHECKS if map is empty
        if self._size == 0:
            return

        # CHECKS if key is in map
        bucket = self.compute_bucket(key)
        result = bucket.contains(key)

        # IF found, key and value is removed
        if result is not None:
            bucket.remove(key)
            self._size -= 1

    def get_keys_and_values(self) -> DynamicArray:
        """
        Returns a Dynamic Array object with all the key and value
        pairs present in the hash map.
        """

        result = DynamicArray()

        # ITERATES through hash table
        for index in range(self._capacity):
            bucket = self._buckets[index]
            if bucket.length() == 0:
                continue

            # ITERATES through bucket
            for node in bucket:
                if node is not None:
                    result.append((node.key, node.value))

        return result

    def clear(self) -> None:
        """
        Clears all elements from the hash map.
        """
        for index in range(self._capacity):
            self._buckets[index] = LinkedList()
        self._size = 0

    def compute_bucket(self, key):
        """
        Takes a key as a parameter and returns the hash computed
        from the current hash map capacity.
        """
        hash = self._hash_function(key)
        ind = hash % self._capacity
        return self._buckets[ind]


def find_mode(da: DynamicArray) -> tuple[DynamicArray, int]:
    """
    Takes a Dynamic Array objects as a parameter and returns
    a tuple containing the mode(s) of the array and the number
    of instances for the mode
    """

    map = HashMap()
    tup = ()

    # CHECKS if array element is in hash map
    for index in range(da.length()):
        bucket = map.compute_bucket(da[index])
        result = bucket.contains(da[index])

        # IF found, increment count
        if result is not None:
            result.value += 1

        # IF not found, add to hash map
        else:
            map.put(da[index], 1)

    # COMPARES elements in array to elements in hash map
    for index in range(da.length()):
        bucket = map.compute_bucket(da[index])
        result = bucket.contains(da[index])

        # IF tuple is not empty
        if len(tup) != 0:

            # IF new mode is found
            if result.value > tup[1]:
                tup = (DynamicArray(0), result.value)
                tup[0].append(result.key)

            # IF additional mode is found
            elif result.value == tup[1]:
                for val in range(tup[0].length()):

                    # CHECKS if new mode is not in tuple
                    if val == tup[0].length() - 1 and tup[0][val] != result.key:
                        tup[0].append(result.key)
                    elif tup[0][val] == result.key:
                        break
        else:
            # IF tuple is empty
            tup = (DynamicArray(), result.value)
            tup[0].append(result.key)

    return tup


# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(53, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
    print(m.get_keys_and_values())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )
    
    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")
