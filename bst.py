# Name: Josue Bustamante
# OSU Email: bustamjo@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 4
# Due Date: 5/20/2024
# Description: A binary search tree class with implementations to add, remove,
#              and search for nodes. In addition, these methods traverse
#              through the tree to find the minimum and maximum values.
#              Finally, methods are included to empty the tree and verify
#              an empty status.


import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.

        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    def print_tree(self):
        """
        Prints the tree using the print_subtree function.

        This method is intended to assist in visualizing the structure of the
        tree. You are encouraged to add this method to the tests in the Basic
        Testing section of the starter code or your own tests as needed.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.get_root():
            self._print_subtree(self.get_root())
        else:
            print('(empty tree)')

    def _print_subtree(self, node, prefix: str = '', branch: str = ''):
        """
        Recursively prints the subtree rooted at this node.

        This is intended as a 'helper' method to assist in visualizing the
        structure of the tree.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        def add_junction(string):
            if len(string) < 2 or branch == '':
                return string
            junction = '|' if string[-2] == '|' else '`'
            return string[:-2] + junction + '-'

        if not node:
            print(add_junction(prefix) + branch + "None")
            return

        if len(prefix) > 2 * 16:
            print(add_junction(prefix) + branch + "(tree continues)")
            return

        if node.left or node.right:
            postfix = ' (root)' if branch == '' else ''
            print(add_junction(prefix) + branch + str(node.value) + postfix)
            self._print_subtree(node.right, prefix + '| ', 'R: ')
            self._print_subtree(node.left, prefix + '  ', 'L: ')
        else:
            print(add_junction(prefix) + branch + str(node.value) + ' (leaf)')

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Takes a value as a parameter and adds a node containing that
        value to the BST.
        """

        cur = self._root

        # CHECKS if BST is empty
        if cur is None:
            self._root = BSTNode(value)
            return

        # ITERATES to appropriate location
        while cur is not None:
            if value < cur.value and cur.left is not None:
                cur = cur.left
            elif value >= cur.value and cur.right is not None:
                cur = cur.right
            else:
                break

        # ADDS value as left node
        if value < cur.value:
            cur.left = BSTNode(value)
            return

        # ADDS value as right node
        elif value >= cur.value:
            cur.right = BSTNode(value)
            return

    def remove(self, value: object) -> bool:
        """
        Takes a value as a parameter and removes the node containing
        that value from the BST, returning True if the operation is
        successful and False otherwise.
        """
        cur = self._root
        par = None

        # CHECKS if BST is empty
        if cur is None:
            return False

        while cur is not None:

            # IF value is found
            if cur.value == value:
                break

            # IF leaf is reached
            if cur.left is None and cur.right is None:
                return False

            # ITERATES to value's location
            par = cur
            if value < cur.value and cur.left is not None:
                cur = cur.left
            elif value > cur.value and cur.right is not None:
                cur = cur.right
            else:
                return False

        # IF node has no subtrees
        if cur.left is None and cur.right is None:
            self._remove_no_subtrees(par, cur)
            return True

        # IF node has one subtree
        if cur.left is None or cur.right is None:
            self._remove_one_subtree(par, cur)
            return True

        # IF node has two subtrees
        if cur.left is not None and cur.right is not None:
            self._remove_two_subtrees(par, cur)
            return True

    def _remove_no_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Takes a target node with no subtrees and its parent as parameters
        and removes the target node from the BST.
        """

        # CHECKS if target node is BST root
        if remove_node == self._root:
            self._root = None
            return

        # FREES node from BST
        if remove_parent.left == remove_node:
            remove_parent.left = None

        elif remove_parent.right == remove_node:
            remove_parent.right = None

    def _remove_one_subtree(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Takes a target node with one subtree and its parent as parameters
        and removes the target node from the BST, adjusting the BST as needed.
        """

        # CHECKS if target node is BST root
        if remove_node == self._root:
            if remove_node.left is not None:
                self._root = self._root.left
            elif remove_node.right is not None:
                self._root = self._root.right

        # IF target node is on the parent's left
        elif remove_parent.left == remove_node:
            if remove_node.left is not None:
                remove_parent.left = remove_node.left
            elif remove_node.right is not None:
                remove_parent.left = remove_node.right

        # IF target node is on the parent's right
        elif remove_parent.right == remove_node:
            if remove_node.left is not None:
                remove_parent.right = remove_node.left
            elif remove_node.right is not None:
                remove_parent.right = remove_node.right

    def _remove_two_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Takes a target node with two subtrees and its parent as parameters
        and removes the target node from the BST, adjusting the BST as needed.
        """
        # FINDS target node's inorder successor
        succ, succ_par = self.find_inorder_successor(remove_node)

        succ.left = remove_node.left
        # IF successor is not target's child
        if succ is not remove_node.right:
            succ_par.left = succ.right
            succ.right = remove_node.right

        # IF target node is the root
        if remove_node == self._root:
            self._root = succ
            return

        # POINTS parent node to successor
        if succ.value < remove_parent.value:
            remove_parent.left = succ
        elif succ.value >= remove_parent.value:
            remove_parent.right = succ

    def find_inorder_successor(self, node):
        """
        Takes a node as a parameter and returns the inorder
        successor of that node as well as the successor's
        parent node.
        """

        # IF there is no inorder successor
        if node.right is None:
            return False

        target = node.right
        parent = node

        # ITERATES to leftmost node in right subtree
        while target is not None:
            if target.left is None:
                return target, parent
            parent = target
            target = target.left

    def contains(self, value: object) -> bool:
        """
        Takes a value as a parameter and returns True if
        a node containing that value is present in the BST.
        """
        cur = self._root

        # CHECKS if BST is empty
        if cur is None:
            return False

        while cur is not None:

            # IF value is found
            if cur.value == value:
                return True

            # IF leaf is reached
            if cur.left is None and cur.right is None:
                return False

            # ITERATES to value's location
            if value < cur.value and cur.left is not None:
                cur = cur.left
            elif value > cur.value and cur.right is not None:
                cur = cur.right
            else:
                return False

    def inorder_traversal(self) -> Queue:
        """
        Returns a Queue object containing the values of nodes visited
        during an inorder traversal of the BST.
        """
        cur = self._root
        arr = Queue()

        # CHECKS if BST is empty
        if cur is None:
            return arr

        # CALLS recursive helper method
        self.rec_inorder_traversal(cur, arr)
        return arr

    def rec_inorder_traversal(self, node, arr):
        """
        Recursive helper method which takes a node and a Queue object
        as parameters and adds the values of the nodes visited during
        an inorder traversal of a BST to the queue.
        """
        if node is not None:
            self.rec_inorder_traversal(node.left, arr)
            arr.enqueue(node.value)
            self.rec_inorder_traversal(node.right, arr)

    def find_min(self) -> object:
        """
        Returns the node containing the minimum value present
        in the BST.
        """
        cur = self._root
        min_node = cur

        # CHECKS if BST is empty
        if cur is None:
            return None

        # CALLS recursive helper method
        result = self.rec_find_min(cur, min_node)
        return result.value

    def rec_find_min(self, node, min_node):
        """
        Recursive helper method which takes a node and the current
        minimum node as parameters and compares the two nodes during
        an inorder traversal of the BST, returning the final minimum
        value node.
        """
        if node.left is not None:
            result = self.rec_find_min(node.left, min_node)
            min_node = result
        if node.value < min_node.value:
            min_node = node
        if node.right is not None:
            result = self.rec_find_min(node.right, min_node)
            min_node = result
        return min_node

    def find_max(self) -> object:
        """
        Returns the node containing the maximum value present
        in the BST.
        """
        cur = self._root
        max_node = cur

        if cur is None:
            return None

        result = self.rec_find_max(cur, max_node)
        return result.value

    def rec_find_max(self, node, max_node):
        """
        Recursive helper method which takes a node and the current
        maximum node as parameters and compares the two nodes during
        an inorder traversal of the BST, returning the final maximum
        value node.
        """
        if node.left is not None:
            result = self.rec_find_max(node.left, max_node)
            max_node = result
        if node.value > max_node.value:
            max_node = node
        if node.right is not None:
            result = self.rec_find_max(node.right, max_node)
            max_node = result
        return max_node

    def is_empty(self) -> bool:
        """
        Returns True is the BST is empty, returning False otherwise.
        """
        if self._root is None:
            return True
        return False

    def make_empty(self) -> None:
        """
        Resets the BST to an empty tree.
        """
        self._root = None


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)
        tree.print_tree()

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
        ((-30, 71, 43, 79, -13, 89, -33, 57, -99, -65), -30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.print_tree()
        tree.remove(del_value)
        print('RESULT :', tree)
        tree.print_tree()
        print('')

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
