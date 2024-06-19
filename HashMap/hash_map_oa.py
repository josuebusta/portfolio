# Name: Josue Bustamante
# OSU Email: bustamjo@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: 6/6/24
# Description: An implementation of an optimized HashMap class of open addressing with quadratic probing capabilities.
#              Includes methods to insert a key and value pair into the Hashmap or remove them,
#              resize or clear the map, and search for keys. Other methods have capabilities to return the load factor,
#              the amount of empty buckets, and an array with the keys and values. Final dunder functions
#              add iteration to the class.

from a6_include import (DynamicArray, DynamicArrayException, HashEntry,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(None)

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
        Increment from given number to find the closest prime number
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
        if self.table_load() >= 0.5:
            new_cap = self._capacity * 2
            self.resize_table(new_cap)

        # CHECKS if key is already in hash map
        index = self.compute_bucket(key)
        bucket = self._buckets[index]

        # IF bucket is empty
        if bucket is None:
            self._buckets.set_at_index(index, HashEntry(key, value))
            self._size += 1
            return

        # IF initial index key matches bucket key
        elif bucket.key == key:
            bucket.value = value
            if bucket.is_tombstone is True:
                bucket.is_tombstone = False
                self._size += 1
            return

        # PROBES map for open bucket
        count = 1
        new_index = self.quad_probe(index, count)
        bucket = self._buckets[new_index]
        while bucket is not None and bucket.is_tombstone is False:

            # IF key matches bucket key
            if bucket.key == key:
                bucket.value = value
                if bucket.is_tombstone is True:
                    bucket.is_tombstone = False
                    self._size += 1
                return

            # RESTART probe process
            count += 1
            new_index = self.quad_probe(index, count)
            bucket = self._buckets[new_index]

        # PUT element in open bucket
        self._buckets.set_at_index(new_index, HashEntry(key, value))
        self._size += 1



    def resize_table(self, new_capacity: int) -> None:
        """
        Takes a new capacity as a parameter and adjusts the table's
        capacity and elements accordingly.
        """

        # CHECKS if new capacity is valid
        if new_capacity < self._size:
            return

        # CHECKS if new capacity is prime
        if self._is_prime(new_capacity) is False:
            new_capacity = self._next_prime(new_capacity)

        # STORES key and value pairs
        kav = self.get_keys_and_values()

        # CLEARS hash map
        self._buckets = DynamicArray()
        self._capacity = new_capacity
        self._size = 0
        for val in range(self._capacity):
            self._buckets.append(None)

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
            bucket = self._buckets[index]
            if bucket is None or bucket.is_tombstone is True:
                count += 1
        return count

    def get(self, key: str) -> object:
        """
        Takes a key as a value and returns the value
        of that key if found in the hash map.
        """

        # CHECKS if map is empty
        if self._size == 0:
            return

        # CHECKS if key is in map
        index = self.compute_bucket(key)
        bucket = self._buckets[index]

        # IF key is found
        if bucket is not None:

            # IF initial key matches active key
            if bucket.key == key and bucket.is_tombstone is False:
                return bucket.value
            # IF initial key matches removed key
            elif bucket.key == key and bucket.is_tombstone is True:
                return
            # IF probe is needed
            else:
                new_bucket = self.quad_probe_search(index, key)

                # IF probe is successful
                if new_bucket is not None:
                    return new_bucket.value

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
        index = self.compute_bucket(key)
        bucket = self._buckets[index]

        # IF key is found
        if bucket is not None:

            # IF initial key matches active key
            if bucket.key == key and bucket.is_tombstone is False:
                return True
            # IF initial key matches removed key
            elif bucket.key == key and bucket.is_tombstone is True:
                return False
            # IF probe is needed
            else:
                new_bucket = self.quad_probe_search(index, key)

                # IF probe is successful
                if new_bucket is not None:
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
        index = self.compute_bucket(key)
        bucket = self._buckets[index]

        # IF key is found
        if bucket is not None:
            # IF initial key matches active key
            if bucket.key == key and bucket.is_tombstone is False:
                bucket.is_tombstone = True
                self._size -= 1
            # IF initial key matches removed key
            elif bucket.key == key and bucket.is_tombstone is True:
                return
            # IF probe is needed
            else:
                new_bucket = self.quad_probe_search(index, key)

                # IF probe is successful
                if new_bucket is not None:
                    new_bucket.is_tombstone = True
                    self._size -= 1

    def get_keys_and_values(self) -> DynamicArray:
        """
        Returns a Dynamic Array object with all the key and value
        pairs present in the hash map.
        """
        result = DynamicArray()

        # ITERATES through hash table
        for index in range(self._capacity):
            if self._buckets[index] is not None and self._buckets[index].is_tombstone is False:
                result.append((self._buckets[index].key, self._buckets[index].value))

        return result

    def clear(self) -> None:
        """
        Clears all elements from the hash map.
        """
        self._buckets = DynamicArray()

        for val in range(self._capacity):
            self._buckets.append(None)
        self._size = 0

    def __iter__(self):
        """
        Creates an iterator for a hash map array
        """
        index = 0
        count = 0
        bucket = self._buckets[index]

        # COMPUTES first index
        while bucket is None or bucket.is_tombstone is True:
            count += 1
            index = self.quad_probe(index, count)
            bucket = self._buckets[index]

        self._index = index
        return self

    def __next__(self):
        """
        Computes next value for iterator.
        """
        try:
            value = self._buckets[self._index]
            # IF end of cluster is reached
            if value is None or value.is_tombstone is True:
                raise StopIteration

        except DynamicArrayException:
            raise StopIteration

        # PROBES for next value
        next_index = self.quad_probe(self._index, 1)
        self._index = next_index

        return value

    def compute_bucket(self, key):
        """
        Takes a key as a parameter and returns the hash computed
        from the current hash map capacity.
        """
        hash = self._hash_function(key)
        ind = hash % self._capacity
        return ind

    def quad_probe(self, index, count):
        num_1 = index + count ** 2
        result = num_1 % self._capacity
        return result

    def quad_probe_search(self, index, key):
        """
        Takes an index and key as parameters and returns the result
        of probing a hash map for the specific keu.
        """
        # CALCULTE quadratic probe
        count = 1
        num_1 = index + count ** 2
        result = num_1 % self._capacity
        bucket = self._buckets[result]


        while bucket is not None:
            # IF key is found in active element
            if bucket.key == key and bucket.is_tombstone is False:
                return bucket
            # IF key is found in inactive element
            elif bucket.key == key and bucket.is_tombstone is False:
                return
            # PROBES to empty spot
            count += 1
            num_1 = index + count ** 2
            result = num_1 % self._capacity
            bucket = self._buckets[result]

        return



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

    print("\nPDF - put example 3")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(15):
        m.put('str' + str(i), i * 100)

    print("\nPDF - put example 4")
    print("-------------------")
    m = HashMap(5, hash_function_1)
    for i in range(5):
        m.put('some key', 'some value')

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
    keys = [i for i in range(25, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        if m.table_load() > 0.5:
            print(f"Check that the load factor is acceptable after the call to resize_table().\n"
                  f"Your load factor is {round(m.table_load(), 2)} and should be less than or equal to 0.5")

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
    m = HashMap(11, hash_function_1)
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

    m.resize_table(2)
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(12)
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

    print("\nPDF - __iter__(), __next__() example 1")
    print("---------------------")
    m = HashMap(10, hash_function_1)
    for i in range(5):
        m.put(str(i), str(i * 10))
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)

    print("\nPDF - __iter__(), __next__() example 2")
    print("---------------------")
    m = HashMap(10, hash_function_2)
    for i in range(5):
        m.put(str(i), str(i * 24))
    m.remove('0')
    m.remove('4')
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)
