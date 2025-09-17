# MinHeap Implementation

An implementation of a minimum binary heap data structure in Python, showcasing efficient priority queue operations, heap property maintenance, and advanced sorting algorithms with optimal time complexity characteristics.

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

- **MinHeap**: A complete minimum binary heap with dynamic array backing
- **DynamicArray**: A resizable array implementation supporting heap operations
- **Heapsort Algorithm**: An in-place sorting algorithm using heap properties

The MinHeap provides efficient O(log n) operations for insertion and deletion, with O(1) access to the minimum element, making it ideal for priority queue implementations and sorting applications.

## Example Output

### MinHeap Operations

```
HEAP [300]
HEAP [285, 300]
HEAP [270, 300, 285]
HEAP [255, 270, 285, 300]
HEAP [240, 255, 285, 300, 270]
HEAP [225, 240, 285, 300, 270, 255]
HEAP [210, 225, 285, 300, 270, 255, 240]
```

### Heap Building

```
HEAP ['zebra', 'apple']
HEAP [6, 20, 100, 200, 90, 150, 300]
```

### Heapsort Example

```
Before: DYN_ARR Size/Cap: 7/8 [100, 20, 6, 200, 90, 150, 300]
After:  DYN_ARR Size/Cap: 7/8 [300, 200, 150, 100, 90, 20, 6]
```

### String Heapsort

```
Before: DYN_ARR Size/Cap: 5/8 ['monkey', 'zebra', 'elephant', 'horse', 'bear']
After:  DYN_ARR Size/Cap: 5/8 ['zebra', 'monkey', 'horse', 'elephant', 'bear']
```

## Features

### MinHeap Features
- **Priority Queue Operations**: Add elements with automatic priority ordering
- **Minimum Access**: O(1) access to the smallest element
- **Efficient Deletion**: O(log n) removal of minimum element
- **Heap Property Maintenance**: Automatic rebalancing after operations
- **Dynamic Sizing**: Automatic capacity management with DynamicArray
- **Exception Handling**: Custom MinHeapException for invalid operations
- **Heap Building**: Efficient construction from existing data

### DynamicArray Features
- **Dynamic Resizing**: Automatic capacity doubling when full
- **Heap Integration**: Optimized for heap operations
- **Memory Management**: Efficient space utilization
- **Array Access**: O(1) indexed access to elements
- **Functional Programming**: Map, filter, and reduce operations

### Advanced Features
- **Heapsort Algorithm**: In-place sorting with O(n log n) complexity
- **Percolate Operations**: Efficient heap property restoration
- **Build Heap**: O(n) heap construction from unsorted data
- **Type Flexibility**: Support for any comparable Python objects
- **Memory Efficiency**: No wasted space with dynamic resizing

## Data Structures

### MinHeap Class
```python
class MinHeap:
    def __init__(self, start_heap=None):
        self._heap = DynamicArray()
```

### DynamicArray Class
```python
class DynamicArray:
    def __init__(self, start_array=None):
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)
```

### Key Methods

#### MinHeap Core Operations
- `add(node)`: Insert element with automatic heap property maintenance
- `get_min()`: Retrieve minimum element without removal
- `remove_min()`: Remove and return minimum element
- `build_heap(da)`: Construct heap from DynamicArray
- `is_empty()`: Check if heap is empty
- `size()`: Get current heap size
- `clear()`: Remove all elements

#### DynamicArray Core Operations
- `append(value)`: Add element to end
- `insert_at_index(index, value)`: Insert at specific position
- `remove_at_index(index)`: Remove element at index
- `resize(new_capacity)`: Change array capacity
- `slice(start_index, size)`: Create subarray
- `map(map_func)`: Apply function to all elements
- `filter(filter_func)`: Select elements based on condition
- `reduce(reduce_func, initializer)`: Combine elements

#### Advanced Functions
- `heapsort(da)`: Sort DynamicArray in non-ascending order
- `_percolate_down(da, parent)`: Restore heap property downward
- `chunk(arr)`: Group consecutive ascending elements
- `find_mode(arr)`: Find most frequent elements

## Installation & Setup

### Prerequisites
- Python 3.7+
- Required dependencies: `static_array` module

### Setup Instructions

1. **Clone or download** the project files
2. **Ensure dependencies** are available:
   ```bash
   # Make sure static_array.py is in the same directory
   # or in your Python path
   ```

3. **Run the implementations**:
   ```bash
   # Run MinHeap implementation
   python min_heap.py
   
   # Run DynamicArray implementation  
   python dynamic_array.py
   ```

## Usage Examples

### Basic MinHeap Operations

```python
from min_heap import MinHeap

# Create a new heap
heap = MinHeap()

# Add elements
heap.add(10)
heap.add(5)
heap.add(15)
heap.add(3)
print(heap)  # HEAP [3, 5, 15, 10]

# Get minimum element
print(heap.get_min())  # 3

# Remove minimum element
min_val = heap.remove_min()
print(f"Removed: {min_val}")  # Removed: 3
print(heap)  # HEAP [5, 10, 15]
```

### Heap Building

```python
from min_heap import MinHeap
from dynamic_array import DynamicArray

# Create heap from existing data
data = DynamicArray([100, 20, 6, 200, 90, 150, 300])
heap = MinHeap()
heap.build_heap(data)
print(heap)  # HEAP [6, 20, 100, 200, 90, 150, 300]

# Initialize with data
heap = MinHeap([53, 25, 21, 44, 66, 52, 18, 39, 97, 51, 32, 42])
print(heap)  # HEAP [18, 25, 21, 39, 32, 42, 53, 44, 97, 51, 66, 52]
```

### Heapsort Algorithm

```python
from min_heap import heapsort
from dynamic_array import DynamicArray

# Sort array in non-ascending order
data = DynamicArray([100, 20, 6, 200, 90, 150, 300])
print(f"Before: {data}")
heapsort(data)
print(f"After: {data}")

# Sort strings
words = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
print(f"Before: {words}")
heapsort(words)
print(f"After: {words}")
```

### Advanced Heap Operations

```python
# Check heap properties
print(heap.is_empty())  # False
print(heap.size())      # 12

# Clear heap
heap.clear()
print(heap.is_empty())  # True

# Work with different data types
string_heap = MinHeap(['fish', 'bird'])
string_heap.add('monkey')
string_heap.add('zebra')
print(string_heap)  # HEAP ['bird', 'fish', 'monkey', 'zebra']
```

### DynamicArray Operations

```python
from dynamic_array import DynamicArray

# Create dynamic array
da = DynamicArray([1, 2, 3, 4, 5])

# Functional programming
squared = da.map(lambda x: x ** 2)
print(squared)  # DYN_ARR Size/Cap: 5/8 [1, 4, 9, 16, 25]

# Filtering
evens = da.filter(lambda x: x % 2 == 0)
print(evens)  # DYN_ARR Size/Cap: 2/4 [2, 4]

# Reducing
total = da.reduce(lambda x, y: x + y)
print(total)  # 15
```

### Complete Example

```python
def priority_queue_example():
    # Create priority queue using MinHeap
    pq = MinHeap()
    
    # Add tasks with priorities
    tasks = [
        (1, "High priority task"),
        (3, "Low priority task"),
        (2, "Medium priority task"),
        (1, "Another high priority task")
    ]
    
    for priority, task in tasks:
        pq.add((priority, task))
    
    # Process tasks in priority order
    while not pq.is_empty():
        priority, task = pq.remove_min()
        print(f"Priority {priority}: {task}")

if __name__ == "__main__":
    priority_queue_example()
```

## Testing

### Running Built-in Tests

Both implementations include comprehensive test suites:

```bash
# Run MinHeap tests
python min_heap.py

# Run DynamicArray tests  
python dynamic_array.py
```

### Test Coverage

The test suites include:

- **Basic Operations**: Add, remove, get_min operations
- **Edge Cases**: Empty heaps, single elements, duplicate values
- **Heap Building**: Construction from various data sets
- **Heapsort**: Sorting with different data types
- **Exception Handling**: Invalid operations and error conditions
- **Performance**: Large data sets and stress testing

### Example Test Output

```
PDF - add example 1
-------------------
HEAP [] True
HEAP [300]
HEAP [285, 300]
HEAP [270, 300, 285]

PDF - remove_min example 1
--------------------------
HEAP [1, 3, 2, 7, 4, 8, 5, 9, 6, 10] 1
HEAP [2, 3, 5, 7, 4, 8, 10, 9, 6] 2
HEAP [3, 4, 5, 7, 6, 8, 10, 9] 3

PDF - heapsort example 1
------------------------
Before: DYN_ARR Size/Cap: 7/8 [100, 20, 6, 200, 90, 150, 300]
After:  DYN_ARR Size/Cap: 7/8 [300, 200, 150, 100, 90, 20, 6]
```

## Performance Analysis

### Time Complexity

| Operation | MinHeap | DynamicArray | Heapsort |
|-----------|---------|--------------|----------|
| Add/Insert | O(log n) | O(1) amortized | N/A |
| Remove Min | O(log n) | O(n) | N/A |
| Get Min | O(1) | O(1) | N/A |
| Build Heap | O(n) | N/A | N/A |
| Sort | N/A | N/A | O(n log n) |
| Access | O(1) | O(1) | N/A |

### Space Complexity
- **MinHeap**: O(n) with dynamic resizing
- **DynamicArray**: O(n) with capacity management
- **Heapsort**: O(1) additional space (in-place)

### Heap Property Maintenance
- **Percolate Up**: O(log n) for insertion
- **Percolate Down**: O(log n) for deletion
- **Heapify**: O(n) for building from array
- **Height**: O(log n) for n elements

### Memory Efficiency
- **Dynamic Resizing**: Doubles capacity when full
- **No Wasted Space**: Only allocates what's needed
- **Cache Performance**: Array-based implementation is cache-friendly
- **Memory Overhead**: Minimal with efficient capacity management

## Learning Outcomes

This project demonstrates:

- **Heap Data Structures**: Understanding of complete binary trees and heap properties
- **Priority Queues**: Implementation of efficient priority-based data access
- **Sorting Algorithms**: Heapsort implementation with optimal complexity
- **Dynamic Memory Management**: Efficient resizing and capacity management
- **Algorithm Analysis**: Time and space complexity considerations
- **Tree Traversal**: Percolate operations for heap maintenance
- **Array-Based Trees**: Efficient tree representation using arrays
- **Functional Programming**: Higher-order functions and data transformation

## References

- [Binary Heap - Wikipedia](https://en.wikipedia.org/wiki/Binary_heap)
- [Priority Queue - Wikipedia](https://en.wikipedia.org/wiki/Priority_queue)
- [Heapsort - Wikipedia](https://en.wikipedia.org/wiki/Heapsort)
- [Complete Binary Tree - GeeksforGeeks](https://www.geeksforgeeks.org/complete-binary-tree/)

---

**Author**: Josue Bustamante  
**Course**: CS261 - Data Structures  
**Institution**: Oregon State University  
**Date**: May 2024