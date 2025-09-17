# Linked List & Abstract Data Types (ADT) Implementation

An implementation of fundamental data structures in Python, showcasing linked list operations, abstract data type design, and multiple implementation strategies for stacks and queues with different underlying data structures.

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

- **Singly Linked List**: A linear data structure with nodes containing data and next pointers
- **Queue ADT (SLL)**: First-in-first-out queue implemented using singly linked list
- **Stack ADT (SLL)**: Last-in-first-out stack implemented using singly linked list
- **Queue ADT (SA)**: Queue implemented using circular buffer static array
- **Stack ADT (DA)**: Stack implemented using dynamic array

All implementations provide efficient O(1) operations for their primary functions, with different trade-offs in memory usage, performance, and implementation complexity.

## Example Output

### Singly Linked List Operations

```
SLL [A -> B -> C]
SLL [D -> A -> B -> C]
SLL [A -> B -> C]
SLL [A -> C]
```

### Queue Operations (SLL)

```
QUEUE []
QUEUE [1 -> 2 -> 3 -> 4 -> 5]
1
2
3
4
5
No elements in queue <class 'QueueException'>
```

### Stack Operations (SLL)

```
STACK []
STACK [1 -> 2 -> 3 -> 4 -> 5]
5
4
3
2
1
Exception: <class 'StackException'>
```

### Queue Operations (SA)

```
QUEUE: 5 element(s). [1, 2, 3, 4, 5]
STAT_ARR Size: 8 [1, 2, 3, 4, 5, None, None, None]
```

### Stack Operations (DA)

```
STACK: 5 elements. [1, 2, 3, 4, 5]
5
4
3
2
1
Exception: <class 'StackException'>
```

## Features

### Singly Linked List Features
- **Node Operations**: Insert at front, back, and specific index
- **Deletion Operations**: Remove by index or by value
- **Search Operations**: Find values and count occurrences
- **Slicing**: Create sublists from original list
- **Exception Handling**: Custom SLLException for invalid operations
- **Memory Efficiency**: Dynamic allocation with no wasted space

### Queue ADT Features (SLL)
- **FIFO Operations**: Enqueue at back, dequeue from front
- **Efficient Access**: O(1) enqueue and dequeue operations
- **Memory Management**: Dynamic allocation with linked list
- **Exception Handling**: QueueException for empty queue operations
- **Simple Implementation**: Straightforward head/tail pointer management

### Stack ADT Features (SLL)
- **LIFO Operations**: Push to top, pop from top
- **Efficient Access**: O(1) push and pop operations
- **Memory Management**: Dynamic allocation with linked list
- **Exception Handling**: StackException for empty stack operations
- **Simple Implementation**: Single head pointer management

### Queue ADT Features (SA)
- **Circular Buffer**: Efficient space utilization with wraparound
- **Dynamic Resizing**: Automatic capacity doubling when full
- **Memory Efficiency**: Fixed-size array with circular indexing
- **Performance**: O(1) operations with array access
- **Space Optimization**: No wasted space in circular buffer

### Stack ADT Features (DA)
- **Dynamic Sizing**: Automatic resizing with dynamic array
- **Efficient Operations**: O(1) push/pop with array access
- **Memory Management**: Automatic capacity management
- **Exception Handling**: StackException for empty stack operations
- **Array Benefits**: Cache-friendly contiguous memory layout

## Data Structures

### Singly Linked List Class
```python
class LinkedList:
    def __init__(self, start_list=None) -> None:
        self._head = SLNode(None)
```

### Queue ADT Classes
```python
# SLL-based Queue
class Queue:
    def __init__(self):
        self._head = None
        self._tail = None

# SA-based Queue
class Queue:
    def __init__(self) -> None:
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0
```

### Stack ADT Classes
```python
# SLL-based Stack
class Stack:
    def __init__(self) -> None:
        self._head = None

# DA-based Stack
class Stack:
    def __init__(self):
        self._da = DynamicArray()
```

### Key Methods

#### Singly Linked List Operations
- `insert_front(value)`: Insert at beginning
- `insert_back(value)`: Insert at end
- `insert_at_index(index, value)`: Insert at specific position
- `remove_at_index(index)`: Remove by index
- `remove(value)`: Remove by value
- `find(value)`: Search for value
- `count(value)`: Count occurrences
- `slice(start_index, size)`: Create sublist

#### Queue Operations
- `enqueue(value)`: Add to back
- `dequeue()`: Remove from front
- `front()`: Peek at front element
- `is_empty()`: Check if empty
- `size()`: Get current size

#### Stack Operations
- `push(value)`: Add to top
- `pop()`: Remove from top
- `top()`: Peek at top element
- `is_empty()`: Check if empty
- `size()`: Get current size

## Installation & Setup

### Prerequisites
- Python 3.7+
- Required dependencies: `SLNode`, `StaticArray`, `DynamicArray` modules

### Setup Instructions

1. **Clone or download** the project files
2. **Ensure dependencies** are available:
   ```bash
   # Make sure SLNode.py, static_array.py, and dynamic_array.py
   # are in the same directory or in your Python path
   ```

3. **Run the implementations**:
   ```bash
   # Run Singly Linked List
   python sll.py
   
   # Run Queue implementations
   python queue_sll.py
   python queue_sa.py
   
   # Run Stack implementations
   python stack_sll.py
   python stack_da.py
   ```

## Usage Examples

### Basic Singly Linked List Operations

```python
from sll import LinkedList

# Create a new linked list
ll = LinkedList()

# Insert elements
ll.insert_front('A')
ll.insert_back('B')
ll.insert_at_index(1, 'C')
print(ll)  # SLL [A -> C -> B]

# Remove elements
ll.remove_at_index(1)
print(ll)  # SLL [A -> B]

# Search operations
print(ll.find('A'))  # True
print(ll.count('B'))  # 1

# Create slice
slice_ll = ll.slice(0, 2)
print(slice_ll)  # SLL [A -> B]
```

### Queue Operations (SLL)

```python
from queue_sll import Queue

# Create a new queue
q = Queue()

# Enqueue elements
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)  # QUEUE [1 -> 2 -> 3]

# Dequeue elements
print(q.dequeue())  # 1
print(q.front())    # 2
print(q.size())     # 2
```

### Stack Operations (SLL)

```python
from stack_sll import Stack

# Create a new stack
s = Stack()

# Push elements
s.push(10)
s.push(20)
s.push(30)
print(s)  # STACK [30 -> 20 -> 10]

# Pop elements
print(s.pop())  # 30
print(s.top())  # 20
print(s.size()) # 2
```

### Queue Operations (SA)

```python
from queue_sa import Queue

# Create a new queue
q = Queue()

# Enqueue elements
for i in range(5):
    q.enqueue(i)
print(q)  # QUEUE: 5 element(s). [0, 1, 2, 3, 4]

# Dequeue elements
print(q.dequeue())  # 0
print(q.front())    # 1
```

### Stack Operations (DA)

```python
from stack_da import Stack

# Create a new stack
s = Stack()

# Push elements
for i in range(5):
    s.push(i)
print(s)  # STACK: 5 elements. [0, 1, 2, 3, 4]

# Pop elements
print(s.pop())  # 4
print(s.top())  # 3
```

### Advanced Usage

```python
# Initialize with data
ll = LinkedList([1, 2, 3, 4, 5])
print(ll)  # SLL [1 -> 2 -> 3 -> 4 -> 5]

# Check if empty
print(ll.is_empty())  # False

# Complex operations
ll.insert_at_index(2, 99)
print(ll)  # SLL [1 -> 2 -> 99 -> 3 -> 4 -> 5]

# Remove by value
ll.remove(99)
print(ll)  # SLL [1 -> 2 -> 3 -> 4 -> 5]

# Create slice
slice_ll = ll.slice(1, 3)
print(slice_ll)  # SLL [2 -> 3 -> 4]
```

## Testing

### Running Built-in Tests

All implementations include comprehensive test suites:

```bash
# Run Singly Linked List tests
python sll.py

# Run Queue tests
python queue_sll.py
python queue_sa.py

# Run Stack tests
python stack_sll.py
python stack_da.py
```

### Test Coverage

The test suites include:

- **Basic Operations**: Insert, remove, access operations
- **Edge Cases**: Empty structures, single elements, boundary conditions
- **Exception Handling**: Invalid operations and error conditions
- **Performance**: Large data sets and stress testing
- **Memory Management**: Resizing and capacity management

### Example Test Output

```
# insert_front example 1
SLL [A]
SLL [B -> A]
SLL [C -> B -> A]

# enqueue example 1
QUEUE []
QUEUE [1 -> 2 -> 3 -> 4 -> 5]

# push example 1
STACK []
STACK [1 -> 2 -> 3 -> 4 -> 5]

# Circular buffer tests
QUEUE: 4 element(s). [2, 4, 6, 8]
STAT_ARR Size: 4 [2, 4, 6, 8]
```

## Performance Analysis

### Time Complexity

| Operation | SLL | Queue (SLL) | Stack (SLL) | Queue (SA) | Stack (DA) |
|-----------|-----|-------------|-------------|------------|------------|
| Insert Front | O(1) | N/A | O(1) | N/A | N/A |
| Insert Back | O(n) | O(1) | N/A | O(1) | N/A |
| Insert Index | O(n) | N/A | N/A | N/A | N/A |
| Remove Front | O(1) | O(1) | N/A | O(1) | N/A |
| Remove Back | O(n) | N/A | N/A | N/A | N/A |
| Remove Index | O(n) | N/A | N/A | N/A | N/A |
| Access | O(n) | O(1) | O(1) | O(1) | O(1) |
| Search | O(n) | N/A | N/A | N/A | N/A |

### Space Complexity
- **SLL**: O(n) with pointer overhead
- **Queue (SLL)**: O(n) with pointer overhead
- **Stack (SLL)**: O(n) with pointer overhead
- **Queue (SA)**: O(n) with potential unused space
- **Stack (DA)**: O(n) with dynamic resizing

### Implementation Trade-offs

#### Singly Linked List
- **Pros**: Dynamic size, efficient front operations
- **Cons**: O(n) back operations, pointer overhead
- **Best For**: Frequent front insertions/deletions

#### Queue (SLL)
- **Pros**: True O(1) operations, dynamic sizing
- **Cons**: Pointer overhead, memory fragmentation
- **Best For**: Variable-size queues

#### Stack (SLL)
- **Pros**: True O(1) operations, dynamic sizing
- **Cons**: Pointer overhead, memory fragmentation
- **Best For**: Variable-size stacks

#### Queue (SA)
- **Pros**: Cache-friendly, no pointer overhead
- **Cons**: Fixed capacity, circular buffer complexity
- **Best For**: Fixed-size queues with resizing

#### Stack (DA)
- **Pros**: Cache-friendly, automatic resizing
- **Cons**: O(n) pop operation, memory overhead
- **Best For**: Large stacks with infrequent pops

## Learning Outcomes

This project demonstrates:

- **Linked List Design**: Understanding of node-based data structures
- **Abstract Data Types**: Implementation of standard ADT interfaces
- **Multiple Implementations**: Different approaches to same functionality
- **Memory Management**: Trade-offs between different data structures
- **Algorithm Analysis**: Time and space complexity considerations
- **Exception Handling**: Robust error management and validation
- **Circular Buffer**: Efficient array-based queue implementation
- **Dynamic Resizing**: Automatic capacity management strategies

## References

- [Linked List - Wikipedia](https://en.wikipedia.org/wiki/Linked_list)
- [Stack (Abstract Data Type) - Wikipedia](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
- [Queue (Abstract Data Type) - Wikipedia](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))
- [Circular Buffer - Wikipedia](https://en.wikipedia.org/wiki/Circular_buffer)

---

**Author**: Josue Bustamante  
**Course**: CS261 - Data Structures  
**Institution**: Oregon State University  
**Date**: May 2024