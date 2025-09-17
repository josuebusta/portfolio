# Dynamic Array & Abstract Data Types (ADT) Implementation

An implementation of fundamental data structures in Python, showcasing dynamic array management, abstract data type design, and functional programming concepts with efficient memory management.

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

This project implements the following data structures:

- **DynamicArray**: A resizable array with automatic capacity management and functional programming methods
- **Bag**: An abstract data type built on DynamicArray for unordered collection management

Both implementations provide efficient O(1) amortized operations for basic array processes, with the DynamicArray featuring functional programming capabilities including mapping, filtering, and reducing operations.

## Example Output

### DynamicArray Operations

```
DYN_ARR Size/Cap: 5/8 [1, 2, 3, 4, 5]
DYN_ARR Size/Cap: 6/8 [100, 1, 2, 3, 4, 5]
DYN_ARR Size/Cap: 4/8 [1, 2, 4, 5]
```

### Bag Operations

```
BAG: 6 elements. [10, 20, 30, 10, 20, 30]
BAG: 5 elements. [10, 20, 30, 10, 20]
BAG: 0 elements. []
```

### Functional Programming Example

```
Original: DYN_ARR Size/Cap: 6/8 [1, 5, 10, 15, 20, 25]
Mapped: DYN_ARR Size/Cap: 6/8 [1, 25, 100, 225, 400, 625]
Filtered: DYN_ARR Size/Cap: 3/8 [15, 20, 25]
```

## Features

### DynamicArray Features
- **Dynamic Resizing**: Automatic capacity doubling when full, halving when under 25% capacity
- **Basic Operations**: Append, insert, remove, and access elements with bounds checking
- **Slicing**: Create subarrays with specified start index and size
- **Functional Programming**: Map, filter, and reduce operations with custom functions
- **Memory Management**: Efficient space utilization with automatic resizing
- **Iterator Support**: Built-in iteration for enhanced usability
- **Exception Handling**: Custom DynamicArrayException for invalid operations

### Bag Features
- **Unordered Collection**: Store elements without maintaining order
- **Duplicate Support**: Allow multiple instances of the same element
- **Element Counting**: Count occurrences of specific elements
- **Equality Testing**: Compare bags for content equality regardless of order
- **Iterator Support**: Iterate through all elements in the bag
- **Dynamic Sizing**: Automatically grows and shrinks based on content

### Advanced Features
- **Chunk Function**: Group consecutive ascending elements into separate arrays
- **Mode Finding**: Identify most frequent elements and their occurrence count
- **Memory Optimization**: Intelligent resizing to prevent excessive memory usage
- **Type Flexibility**: Support for any Python object type

## Data Structures

### DynamicArray Class
```python
class DynamicArray:
    def __init__(self, start_array=None):
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)
```

### Bag Class
```python
class Bag:
    def __init__(self, start_bag=None):
        self._da = DynamicArray()
```

### Key Methods

#### DynamicArray Core Methods
- `append(value)`: Add element to end
- `insert_at_index(index, value)`: Insert at specific position
- `remove_at_index(index)`: Remove element at index
- `slice(start_index, size)`: Create subarray
- `map(map_func)`: Apply function to all elements
- `filter(filter_func)`: Select elements based on condition
- `reduce(reduce_func, initializer)`: Combine elements into single value

#### Bag Core Methods
- `add(value)`: Add element to bag
- `remove(value)`: Remove first occurrence of element
- `count(value)`: Count occurrences of element
- `clear()`: Remove all elements
- `equal(other_bag)`: Check if bags contain same elements

## Installation & Setup

### Prerequisites
- Python 3.7+
- Required dependency: `static_array` module

### Setup Instructions

1. **Clone or download** the project files
2. **Ensure dependencies** are available:
   ```bash
   # Make sure static_array.py is in the same directory
   # or in your Python path
   ```

3. **Run the implementations**:
   ```bash
   # Run DynamicArray implementation
   python dynamic_array.py
   
   # Run Bag implementation  
   python bag_da.py
   ```

## Usage Examples

### Basic DynamicArray Operations

```python
from dynamic_array import DynamicArray

# Create a new dynamic array
da = DynamicArray()

# Add elements
da.append(1)
da.append(2)
da.append(3)
print(da)  # DYN_ARR Size/Cap: 3/4 [1, 2, 3]

# Insert at specific index
da.insert_at_index(1, 10)
print(da)  # DYN_ARR Size/Cap: 4/4 [1, 10, 2, 3]

# Remove element
da.remove_at_index(1)
print(da)  # DYN_ARR Size/Cap: 3/4 [1, 2, 3]

# Access elements
print(da[0])  # 1
print(da.length())  # 3
```

### Advanced DynamicArray Operations

```python
# Create array with initial data
da = DynamicArray([1, 2, 3, 4, 5])

# Slice operation
slice_da = da.slice(1, 3)
print(slice_da)  # DYN_ARR Size/Cap: 3/4 [2, 3, 4]

# Map operation (square all elements)
squared = da.map(lambda x: x ** 2)
print(squared)  # DYN_ARR Size/Cap: 5/8 [1, 4, 9, 16, 25]

# Filter operation (keep only even numbers)
evens = da.filter(lambda x: x % 2 == 0)
print(evens)  # DYN_ARR Size/Cap: 2/4 [2, 4]

# Reduce operation (sum all elements)
total = da.reduce(lambda x, y: x + y)
print(total)  # 15
```

### Bag Operations

```python
from bag_da import Bag

# Create a new bag
bag = Bag()

# Add elements
bag.add(10)
bag.add(20)
bag.add(10)
bag.add(30)
print(bag)  # BAG: 4 elements. [10, 20, 10, 30]

# Count occurrences
print(bag.count(10))  # 2
print(bag.count(20))  # 1

# Remove elements
bag.remove(10)
print(bag)  # BAG: 3 elements. [20, 10, 30]

# Check equality
bag1 = Bag([1, 2, 3, 2])
bag2 = Bag([2, 1, 3, 2])
print(bag1.equal(bag2))  # True

# Iterate through bag
for item in bag:
    print(item)  # 20, 10, 30
```

### Advanced Usage

```python
# Initialize with data
da = DynamicArray([1, 2, 3, 4, 5])
bag = Bag([10, 20, 30, 10, 20])

# Check if empty
print(da.is_empty())  # False
print(bag.size())     # 5

# Clear collections
da.clear()  # Not implemented, but bag has clear()
bag.clear()
print(bag.size())  # 0

# Chunk function
da = DynamicArray([1, 2, 3, 1, 2, 4, 5, 6])
chunked = chunk(da)
print(chunked)  # Array of ascending chunks

# Find mode
da = DynamicArray([1, 1, 2, 3, 3, 3, 4])
mode, frequency = find_mode(da)
print(f"Mode: {mode}, Frequency: {frequency}")
```

## Testing

### Running Built-in Tests

Both implementations include comprehensive test suites:

```bash
# Run DynamicArray tests
python dynamic_array.py

# Run Bag tests  
python bag_da.py
```

### Test Coverage

The test suites include:

- **Basic Operations**: Append, insert, remove, access
- **Edge Cases**: Empty arrays, single elements, boundary conditions
- **Resizing**: Capacity changes and memory management
- **Functional Programming**: Map, filter, reduce operations
- **Error Handling**: Invalid indices and exception testing
- **Performance**: Large data sets and stress testing

### Example Test Output

```
# append - example 1
Length: 0, Capacity: 4, [None, None, None, None]
Length: 1, Capacity: 4, [1, None, None, None]
DYN_ARR Size/Cap: 1/4 [1]

# map example 1
DYN_ARR Size/Cap: 6/8 [1, 5, 10, 15, 20, 25]
DYN_ARR Size/Cap: 6/8 [1, 25, 100, 225, 400, 625]

# bag equal example 1
BAG: 6 elements. [10, 20, 30, 40, 50, 60]
BAG: 6 elements. [60, 50, 40, 30, 20, 10]
True True
```

## Performance Analysis

### Time Complexity

| Operation | DynamicArray | Bag |
|-----------|--------------|-----|
| Append    | O(1) amortized | O(1) amortized |
| Insert    | O(n) | O(1) amortized |
| Remove    | O(n) | O(n) |
| Access    | O(1) | O(1) |
| Search    | O(n) | O(n) |
| Map       | O(n) | O(n) |
| Filter    | O(n) | O(n) |
| Reduce    | O(n) | O(n) |

### Space Complexity
- **Space**: O(n) for both implementations
- **Capacity**: O(n) with automatic resizing
- **Memory Efficiency**: Maintains 25-100% capacity utilization

### Resizing Strategy
- **Growth**: Double capacity when full
- **Shrink**: Halve capacity when under 25% full
- **Minimum**: Maintain minimum capacity of 4 elements
- **Amortized Cost**: O(1) per operation over sequence of operations

## Learning Outcomes

This project demonstrates:

- **Dynamic Memory Management**: Understanding of resizable data structures
- **Abstract Data Types**: Design and implementation of collection interfaces
- **Functional Programming**: Higher-order functions and data transformation
- **Algorithm Analysis**: Time and space complexity considerations
- **Object-Oriented Design**: Clean class hierarchies and encapsulation
- **Exception Handling**: Robust error management and validation
- **Iterator Pattern**: Implementation of iteration protocols
- **Memory Optimization**: Efficient space utilization strategies

## References

- [Dynamic Array - Wikipedia](https://en.wikipedia.org/wiki/Dynamic_array)
- [Abstract Data Type - Wikipedia](https://en.wikipedia.org/wiki/Abstract_data_type)
- [Functional Programming in Python](https://docs.python.org/3/howto/functional.html)
- [Python Iterator Protocol](https://docs.python.org/3/library/stdtypes.html#iterator-types)

---

**Author**: Josue Bustamante  
**Course**: CS261 - Data Structures  
**Institution**: Oregon State University  
**Date**: April 2024