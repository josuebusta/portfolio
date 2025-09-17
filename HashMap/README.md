# HashMap Implementation

An implementation of two fundamental hash table data structures in Python, showcasing efficient key-value storage, collision resolution strategies, and dynamic resizing with optimal performance characteristics.

## Table of Contents

- [Overview](#overview)
- [Example Output](#example-output)
- [Features](#features)
- [Data Structures](#data-structures)
- [Installation & Setup](#installation--setup)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Performance Analysis](#performance-analysis)
- [Learning Outcomes](#learning-outcomes)
- [References](#references)

## Overview

This project implements the following hash table data structures:

- **Open Addressing HashMap**: Uses quadratic probing for collision resolution with tombstone deletion
- **Separate Chaining HashMap**: Uses linked lists for collision resolution with dynamic resizing

Both implementations provide efficient O(1) average-case operations for insertion, deletion, and lookup, with the open addressing version featuring automatic resizing and the chaining version supporting higher load factors.

## Example Output

### Open Addressing HashMap

```
0: None
1: None
2: HashEntry(key='key1', value=10, is_tombstone=False)
3: None
4: HashEntry(key='key2', value=20, is_tombstone=False)
5: None
```

### Separate Chaining HashMap

```
0: None
1: None
2: LL -> key1:10 -> None
3: None
4: LL -> key2:20 -> None
5: None
```

### Mode Finding Example

```
Input: DYN_ARR Size/Cap: 5/8 ['apple', 'apple', 'grape', 'melon', 'peach']
Mode : DYN_ARR Size/Cap: 1/4 ['apple'], Frequency: 2
```

## Features

### Open Addressing Features
- **Quadratic Probing**: Efficient collision resolution with quadratic sequence
- **Tombstone Deletion**: Mark deleted entries without affecting probe sequences
- **Automatic Resizing**: Doubles capacity when load factor reaches 0.5
- **Prime Capacity**: Ensures optimal hash distribution with prime number capacity
- **Iterator Support**: Built-in iteration over active entries
- **Load Factor Management**: Maintains optimal performance with controlled resizing

### Separate Chaining Features
- **Linked List Buckets**: Store multiple entries per bucket using linked lists
- **Higher Load Factor**: Supports load factors up to 1.0 before resizing
- **Dynamic Resizing**: Doubles capacity when load factor reaches 1.0
- **Efficient Collision Handling**: No clustering issues with chaining approach
- **Memory Efficiency**: Only allocates space for actual entries
- **Simple Implementation**: Straightforward collision resolution logic

### Advanced Features
- **Mode Finding**: Efficiently find most frequent elements using hash tables
- **Hash Function Support**: Multiple hash function implementations
- **Prime Number Utilities**: Automatic prime number generation for optimal capacity
- **Comprehensive Statistics**: Load factor, empty buckets, and size tracking
- **Key-Value Extraction**: Retrieve all stored key-value pairs

## Data Structures

### Open Addressing HashMap Class
```python
class HashMap:
    def __init__(self, capacity: int, function) -> None:
        self._buckets = DynamicArray()
        self._capacity = self._next_prime(capacity)
        self._hash_function = function
        self._size = 0
```

### Separate Chaining HashMap Class
```python
class HashMap:
    def __init__(self, capacity: int = 11, function = hash_function_1) -> None:
        self._buckets = DynamicArray()
        self._capacity = self._next_prime(capacity)
        self._hash_function = function
        self._size = 0
```

### Key Methods

#### Core HashMap Operations
- `put(key, value)`: Insert or update key-value pair
- `get(key)`: Retrieve value by key
- `remove(key)`: Delete key-value pair
- `contains_key(key)`: Check if key exists
- `resize_table(new_capacity)`: Resize hash table
- `clear()`: Remove all entries

#### Utility Methods
- `table_load()`: Calculate current load factor
- `empty_buckets()`: Count empty buckets
- `get_keys_and_values()`: Extract all key-value pairs
- `compute_bucket(key)`: Calculate bucket index for key

#### Specialized Functions
- `find_mode(da)`: Find most frequent elements in DynamicArray
- `_next_prime(capacity)`: Find next prime number
- `_is_prime(capacity)`: Check if number is prime

## Installation & Setup

### Prerequisites
- Python 3.7+
- Required dependencies: `a6_include` module with DynamicArray, LinkedList, and hash functions

### Setup Instructions

1. **Clone or download** the project files
2. **Ensure dependencies** are available:
   ```bash
   # Make sure a6_include.py is in the same directory
   # or in your Python path
   ```

3. **Run the implementations**:
   ```bash
   # Run Open Addressing HashMap
   python hash_map_oa.py
   
   # Run Separate Chaining HashMap  
   python hash_map_sc.py
   ```

## Usage Examples

### Basic Open Addressing Operations

```python
from hash_map_oa import HashMap, hash_function_1

# Create a new hash map
hm = HashMap(11, hash_function_1)

# Insert key-value pairs
hm.put('key1', 10)
hm.put('key2', 20)
hm.put('key3', 30)
print(f"Size: {hm.get_size()}, Capacity: {hm.get_capacity()}")

# Retrieve values
print(hm.get('key1'))  # 10
print(hm.get('key2'))  # 20

# Check if key exists
print(hm.contains_key('key1'))  # True
print(hm.contains_key('key4'))  # False

# Remove entries
hm.remove('key2')
print(hm.contains_key('key2'))  # False
```

### Basic Separate Chaining Operations

```python
from hash_map_sc import HashMap, hash_function_1

# Create a new hash map
hm = HashMap(11, hash_function_1)

# Insert key-value pairs
hm.put('apple', 5)
hm.put('banana', 3)
hm.put('cherry', 8)
print(f"Load factor: {hm.table_load():.2f}")

# Retrieve values
print(hm.get('apple'))  # 5
print(hm.get('banana'))  # 3

# Get all key-value pairs
pairs = hm.get_keys_and_values()
print(pairs)  # DynamicArray with tuples
```

### Advanced Operations

```python
# Resize hash table
print(f"Before resize: {hm.get_capacity()}")
hm.resize_table(23)
print(f"After resize: {hm.get_capacity()}")

# Check load factor and empty buckets
print(f"Load factor: {hm.table_load():.2f}")
print(f"Empty buckets: {hm.empty_buckets()}")

# Clear hash map
hm.clear()
print(f"After clear: {hm.get_size()}")
```

### Mode Finding

```python
from hash_map_sc import find_mode
from dynamic_array import DynamicArray

# Find mode in array
data = DynamicArray(['apple', 'banana', 'apple', 'cherry', 'banana', 'apple'])
mode, frequency = find_mode(data)
print(f"Mode: {mode}, Frequency: {frequency}")

# Mode with numbers
numbers = DynamicArray([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
mode, frequency = find_mode(numbers)
print(f"Mode: {mode}, Frequency: {frequency}")
```

### Iterator Usage

```python
# Iterate through open addressing hash map
hm = HashMap(11, hash_function_1)
hm.put('a', 1)
hm.put('b', 2)
hm.put('c', 3)

for entry in hm:
    print(f"Key: {entry.key}, Value: {entry.value}")
```

## Testing

### Running Built-in Tests

Both implementations include comprehensive test suites:

```bash
# Run Open Addressing tests
python hash_map_oa.py

# Run Separate Chaining tests  
python hash_map_sc.py
```

### Test Coverage

The test suites include:

- **Basic Operations**: Put, get, remove, contains_key
- **Edge Cases**: Empty maps, single entries, duplicate keys
- **Resizing**: Capacity changes and load factor management
- **Collision Handling**: Multiple keys with same hash
- **Performance**: Large data sets and stress testing
- **Mode Finding**: Various data types and edge cases

### Example Test Output

```
PDF - put example 1
-------------------
39 0.5 25 53
14 0.5 50 101
0 0.5 75 151
0 0.5 100 151
0 0.5 125 151
0 0.5 150 151

PDF - table_load example 1
--------------------------
0.0
0.01
0.02
0.02

PDF - find_mode example 1
-----------------------------
Input: DYN_ARR Size/Cap: 5/8 ['apple', 'apple', 'grape', 'melon', 'peach']
Mode : DYN_ARR Size/Cap: 1/4 ['apple'], Frequency: 2
```

## Performance Analysis

### Time Complexity

| Operation | Open Addressing | Separate Chaining |
|-----------|----------------|-------------------|
| Insert    | O(1) average   | O(1) average      |
| Search    | O(1) average   | O(1) average      |
| Delete    | O(1) average   | O(1) average      |
| Resize    | O(n)          | O(n)              |
| Mode Find | O(n)          | O(n)              |

### Space Complexity
- **Space**: O(n) for both implementations
- **Load Factor**: 0.5 max for open addressing, 1.0 max for chaining
- **Memory Overhead**: Minimal for chaining, tombstone overhead for open addressing

### Collision Resolution Comparison

#### Open Addressing (Quadratic Probing)
- **Pros**: Cache-friendly, no extra memory for pointers
- **Cons**: Clustering issues, tombstone overhead
- **Best For**: Memory-constrained environments

#### Separate Chaining
- **Pros**: No clustering, simple deletion, higher load factors
- **Cons**: Extra memory for pointers, cache misses
- **Best For**: High-performance applications with memory available

### Hash Function Performance
- **Hash Function 1**: Simple character-based hashing
- **Hash Function 2**: More complex polynomial hashing
- **Prime Capacity**: Ensures uniform distribution

## Learning Outcomes

This project demonstrates:

- **Hash Table Design**: Understanding of key-value storage mechanisms
- **Collision Resolution**: Different strategies for handling hash collisions
- **Dynamic Resizing**: Automatic capacity management for optimal performance
- **Load Factor Management**: Balancing space and time efficiency
- **Prime Number Mathematics**: Using prime numbers for optimal hashing
- **Algorithm Analysis**: Time and space complexity considerations
- **Data Structure Comparison**: Trade-offs between different implementations
- **Memory Management**: Efficient use of memory with different approaches

## References

- [Hash Table - Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
- [Open Addressing - Wikipedia](https://en.wikipedia.org/wiki/Open_addressing)
- [Separate Chaining - Wikipedia](https://en.wikipedia.org/wiki/Hash_table#Separate_chaining)
- [Quadratic Probing - GeeksforGeeks](https://www.geeksforgeeks.org/quadratic-probing-in-hashing/)

---

**Author**: Josue Bustamante  
**Course**: CS261 - Data Structures  
**Institution**: Oregon State University  
**Date**: June 2024