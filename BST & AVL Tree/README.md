# Binary Search Tree (BST) & AVL Tree Implementation

An implementation of two fundamental tree data structures in Python, showcasing efficient search, insertion, and deletion operations with proper balancing mechanisms.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Data Structures](#data-structures)
- [Installation & Setup](#installation--setup)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Performance Analysis](#performance-analysis)
- [Example Output](#example-output)

## Overview

This project implements two critical tree data structures:

- **Binary Search Tree (BST)**: A basic tree structure that maintains the binary search property
- **AVL Tree**: A self-balancing binary search tree that maintains logarithmic height through rotations

Both implementations provide efficient O(log n) average-case operations for search, insertion, and deletion, with the AVL tree guaranteeing O(log n) worst-case performance through automatic rebalancing.

## Features

### BST Features
- **Insertion**: Add elements while maintaining BST property
- **Deletion**: Remove elements with three cases (no children, one child, two children)
- **Search**: Find elements efficiently
- **Traversal**: In-order traversal returning a Queue
- **Min/Max**: Find minimum and maximum values
- **Validation**: Built-in BST property verification
- **Visualization**: Tree structure printing for debugging

### AVL Tree Features
- **All BST Features**: Inherits all functionality from BST
- **Self-Balancing**: Automatic rebalancing after insertions/deletions
- **Height Tracking**: Maintains node heights for balance calculations
- **Rotation Operations**: Left, right, and double rotations
- **Balance Factor**: Calculates and maintains balance factors
- **Parent Pointers**: Bidirectional node relationships for efficient traversal

## Data Structures

### BSTNode Class
```python
class BSTNode:
    def __init__(self, value: object) -> None:
        self.value = value    # Node data
        self.left = None      # Left child pointer
        self.right = None     # Right child pointer
```

### AVLNode Class (extends BSTNode)
```python
class AVLNode(BSTNode):
    def __init__(self, value: object) -> None:
        super().__init__(value)
        self.parent = None    # Parent pointer for efficient traversal
        self.height = 0       # Height tracking for balance
```

## Installation & Setup

### Prerequisites
- Python 3.7+
- Required dependency: `queue_and_stack` module

### Setup Instructions

1. **Clone or download** the project files
2. **Ensure dependencies** are available:
   ```bash
   # Make sure queue_and_stack.py is in the same directory
   # or in your Python path
   ```

3. **Run the implementations**:
   ```bash
   # Run BST implementation
   python bst.py
   
   # Run AVL implementation  
   python avl.py
   ```

## Usage Examples

### Basic BST Operations

```python
from bst import BST

# Create a new BST
tree = BST()

# Add elements
tree.add(50)
tree.add(30)
tree.add(70)
tree.add(20)
tree.add(40)
tree.add(60)
tree.add(80)

# Search for elements
print(tree.contains(40))  # True
print(tree.contains(45))  # False

# Find min/max
print(tree.find_min())    # 20
print(tree.find_max())    # 80

# In-order traversal
print(tree.inorder_traversal())  # Queue with sorted elements

# Remove elements
tree.remove(40)
print(tree.contains(40))  # False

# Visualize tree structure
tree.print_tree()
```

### AVL Tree Operations

```python
from avl import AVL

# Create a new AVL tree
avl_tree = AVL()

# Add elements (automatic balancing)
avl_tree.add(50)
avl_tree.add(30)
avl_tree.add(70)
avl_tree.add(20)
avl_tree.add(40)
avl_tree.add(60)
avl_tree.add(80)

# All BST operations work the same
print(avl_tree.contains(40))  # True
print(avl_tree.find_min())    # 20

# AVL-specific validation
print(avl_tree.is_valid_avl())  # True

# Visualize balanced tree
avl_tree.print_tree()
```

### Advanced Usage

```python
# Initialize with data
bst = BST([10, 5, 15, 3, 7, 12, 18])
avl = AVL([10, 5, 15, 3, 7, 12, 18])

# Check if trees are empty
print(bst.is_empty())  # False

# Clear trees
bst.make_empty()
avl.make_empty()
print(bst.is_empty())  # True
```

## Testing

### Running Built-in Tests

Both implementations include comprehensive test suites:

```bash
# Run BST tests
python bst.py

# Run AVL tests  
python avl.py
```

### Test Coverage

The test suites include:

- **Basic Operations**: Add, remove, search, min/max
- **Edge Cases**: Empty trees, single nodes, duplicates
- **Stress Testing**: Random data sets with validation
- **Tree Validation**: BST/AVL property verification
- **Visualization**: Tree structure printing for manual inspection

### Example Test Output

```
PDF - method add() example 1
----------------------------
BST pre-order { 1, 2, 3 }
    1 (root)
    R: 2
        R: 3 (leaf)

PDF - method remove() example 1
-------------------------------
INPUT  : BST pre-order { 1, 2, 3 } DEL: 1
RESULT : BST pre-order { 2, 3 }
```

## Performance Analysis

### Time Complexity

| Operation | BST (Average) | BST (Worst) | AVL (Worst) |
|-----------|---------------|-------------|-------------|
| Search    | O(log n)      | O(n)        | O(log n)    |
| Insert    | O(log n)      | O(n)        | O(log n)    |
| Delete    | O(log n)      | O(n)        | O(log n)    |
| Min/Max   | O(log n)      | O(n)        | O(log n)    |

### Space Complexity
- **Space**: O(n) for both implementations
- **Height**: O(log n) for AVL, O(n) worst-case for BST

### Tree Visualization Example

```
BST pre-order { 50, 30, 20, 40, 70, 60, 80 }
    50 (root)
    L: 30
        L: 20 (leaf)
        R: 40 (leaf)
    R: 70
        L: 60 (leaf)
        R: 80 (leaf)
```

## Example Output

### AVL Tree After Balancing

```
AVL pre-order { 50, 30, 20, 40, 70, 60, 80 }
    50 (root)
    L: 30
        L: 20 (leaf)
        R: 40 (leaf)
    R: 70
        L: 60 (leaf)
        R: 80 (leaf)
```

## Learning Outcomes

This project demonstrates:

- **Tree Data Structures**: Understanding of hierarchical data organization
- **Search Algorithms**: Efficient element location strategies
- **Balancing Techniques**: Maintaining optimal tree structure
- **Object-Oriented Design**: Clean class hierarchies and inheritance
- **Algorithm Analysis**: Time and space complexity considerations
- **Code Organization**: Modular design with helper methods

## References

- [Binary Search Tree - Wikipedia](https://en.wikipedia.org/wiki/Binary_search_tree)
- [AVL Tree - Wikipedia](https://en.wikipedia.org/wiki/AVL_tree)
- [Tree Rotations - GeeksforGeeks](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/)

---

**Author**: Josue Bustamante  
**Course**: CS261 - Data Structures  
**Institution**: Oregon State University  
**Date**: May 2024
