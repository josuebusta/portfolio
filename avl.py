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
from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Takes a value as a parameter and adds it to the tree while
        maintaining its AVL property.
        """
        cur = self._root

        # CHECKS if AVL tree is empty
        if cur is None:
            self._root = AVLNode(value)
            return


        while cur is not None:

            # IF duplicate value is found
            if value == cur.value:
                return

            # ITERATES to appropriate location
            if value < cur.value and cur.left is not None:
                cur = cur.left
            elif value > cur.value and cur.right is not None:
                cur = cur.right
            else:
                break

        # ADDS value as left node
        if value < cur.value:
            new_node = AVLNode(value)
            cur.left = new_node
            new_node.parent = cur

        # ADDS value as right node
        elif value >= cur.value:
            new_node = AVLNode(value)
            cur.right = new_node
            new_node.parent = cur

        # REBALANCES AVL tree
        nn_parent = new_node.parent
        while nn_parent is not None:
            self._rebalance(nn_parent)
            nn_parent = nn_parent.parent


    def remove(self, value: object) -> bool:
        """
        Takes a value as a parameter and removes the node containing
        the specified value from the AVL tree, returning True if
        the operation was successful and False otherwise.
        """
        cur = self._root

        # CHECKS if AVL tree is empty
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
            if value < cur.value and cur.left is not None:
                cur = cur.left
            elif value > cur.value and cur.right is not None:
                cur = cur.right
            else:
                return False

        # IF target node has no subtrees
        if cur.left is None and cur.right is None:
            self._remove_no_subtrees(cur.parent, cur)


        # IF target node has one subtree
        elif cur.left is None or cur.right is None:
            self._remove_one_subtree(cur.parent, cur)

            # POINTS child node to parent node
            n_root = cur.parent
            if n_root is not None:
                if n_root.left is not None:
                    n_root.left.parent = n_root
                elif n_root.right is not None:
                    n_root.right.parent = n_root

        # IF target node has two subtrees
        elif cur.left is not None and cur.right is not None:
            succ = self._remove_two_subtrees(cur.parent, cur)

            nn_parent = succ

            # REBALANCES AVL tree
            while nn_parent is not None:
                self._rebalance(nn_parent)
                nn_parent = nn_parent.parent
            return True




        nn_parent = cur.parent

        # REBALANCES AVL tree
        while nn_parent is not None:
            self._rebalance(nn_parent)
            nn_parent = nn_parent.parent
        return True

    def _remove_two_subtrees(self, remove_parent: AVLNode, remove_node: AVLNode) -> AVLNode:
        """
        Takes a target node with two subtrees and its parent node as parameters
        and removes the target node from the AVL tree.
        """

        # FINDS inorder successor node and its parent
        succ, succ_par = self.find_inorder_successor(remove_node)

        succ.left = remove_node.left
        # IF successor is not target's child
        if succ is not remove_node.right:

            succ_par.left = succ.right
            if succ.right is not None:
                succ.right.parent = succ_par

            succ.right = remove_node.right
            if remove_node.right is not None:
                remove_node.right.parent = succ

        # IF target node is the AVL tree's root
        if remove_node == self._root:
            self._root = succ
            succ.parent = None

            # RETURNS lowest modified node
            if succ_par.left == succ or succ_par.right == succ:
                return succ
            return succ_par

        # POINTS parent node to successor

        if succ.value < remove_parent.value:
            remove_parent.left = succ
            succ.parent = remove_parent
        elif succ.value >= remove_parent.value:
            remove_parent.right = succ
            succ.parent = remove_parent
        return succ


    def _balance_factor(self, node: AVLNode) -> int:
        """
        Takes a node as a parameter and returns its balance factor.
        """
        # CALCULATES right node height - left node height
        result = self._get_height(node.right) - self._get_height(node.left)
        return result

    def _get_height(self, node: AVLNode) -> int:
        """
        Takes a node as a parameter and returns its height.
        """

        # IF node does not exist
        if node is None:
            return -1

        return node.height


    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """
        Takes a target node as a parameter and performs a left rotation,
        returning the node rotated around the target node.
        """

        node_rotated = node.right
        node.right = node_rotated.left
        if node.right is not None:
            node.right.parent = node
        node_rotated.left = node
        node_rotated.parent = node.parent
        node.parent = node_rotated

        # IF target node was the root
        if self.get_root() == node:
            self._root = node_rotated

        # UPDATES node heights
        self._update_height(node)
        self._update_height(node_rotated)
        return node_rotated



    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """
        Takes a target node as a parameter and performs a right rotation,
        returning the node rotated around the target node.
        """
        node_rotated = node.left
        node.left = node_rotated.right
        if node.left is not None:
            node.left.parent = node
        node_rotated.right = node
        node_rotated.parent = node.parent
        node.parent = node_rotated

        # IF target node was the root
        if self.get_root() == node:
            self._root = node_rotated

        # UPDATES node heights
        self._update_height(node)
        self._update_height(node_rotated)
        return node_rotated

    def _update_height(self, node: AVLNode) -> None:
        """
        Takes a node as a parameter and updates its height based
        on the height if its child nodes.
        """

        # GETS child nodes' heights
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)

        # ADDS 1 + maximum child node height
        if left_height > right_height:
            node.height = left_height + 1
        elif left_height <= right_height:
            node.height = right_height + 1


    def _rebalance(self, node: AVLNode) -> None:
        """
        Takes a node as a parameter and rebalances it if the
        balance factor is beyond the limits for an AVL tree.
        """
        # CHECKS if node is left heavy
        if self._balance_factor(node) < -1:
            # CHECKS if double rotation is needed
            if self._balance_factor(node.left) > 0:
                node.left = self._rotate_left(node.left)
                node.left.parent = node
            new_stroot = self._rotate_right(node)

            # POINTS parent node to child
            if new_stroot.parent is not None:
                if new_stroot.value < new_stroot.parent.value:
                    new_stroot.parent.left = new_stroot
                elif new_stroot.value >= new_stroot.parent.value:
                    new_stroot.parent.right = new_stroot

        # CHECKS if node is right heavy
        elif self._balance_factor(node) > 1:
            # CHECKS if double rotation is needed
            if self._balance_factor(node.right) < 0:
                node.right = self._rotate_right(node.right)
                node.right.parent = node
            new_stroot = self._rotate_left(node)

            # POINTS parent node to child
            if new_stroot.parent is not None:
                if new_stroot.value < new_stroot.parent.value:
                    new_stroot.parent.left = new_stroot
                elif new_stroot.value >= new_stroot.parent.value:
                    new_stroot.parent.right = new_stroot
        else:
            self._update_height(node)

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)
        tree.print_tree()

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', tree)
    """
    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')
    """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.print_tree()
        tree.remove(del_value)
        print('RESULT :', tree)
        tree.print_tree()
        print('')
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        print('RESULT :', tree)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")

    tree = AVL((96, 65, -29, 36, -58, 43, 19, 88, 25, 95))
    tree.remove(96)
    if not tree.is_valid_avl():
        raise Exception("PROBLEM WITH REMOVE OPERATION")
    tree.remove(-29)
    if not tree.is_valid_avl():
        raise Exception("PROBLEM WITH REMOVE OPERATION")
    tree.remove(-58)
    if not tree.is_valid_avl():
        raise Exception("PROBLEM WITH REMOVE OPERATION")

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(5):
        case = list(set(random.randrange(1, 99) for _ in range(5)))
        tree = AVL(case)
        for value in case[::2]:
            tree.remove(value)
            if not tree.is_valid_avl():
                raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
