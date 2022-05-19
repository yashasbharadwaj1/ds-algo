# Import required functions
from collections import deque
from binary_tree import *
from binary_tree_node import *

# Using two queues
def level_order_traversal(root):
    #   We print None if the root is None
    if not root:
        print("None", end="")
    else:
        result = ""
        
        # Declaring an array of two queues
        queues = [deque(), deque()]

        # Initializing the current and next queues
        current_queue = queues[0]
        next_queue = queues[1]

        # Enqueuing the root node into the current queue and setting
        # level to zero   
        current_queue.append(root)
        level_number = 0

        # Printing nodes in level-order until the current queue remains
        # empty
        while current_queue:
            # Dequeuing and printing the first element of queue
            temp = current_queue.popleft()
            print(str(temp.data), end="")
            result += str(temp.data) + ""

            # Adding dequeued node's children to the next queue
            if temp.left:
                next_queue.append(temp.left)

            if temp.right:
                next_queue.append(temp.right)

            # When the current queue is empty, we increase the level, print a new line
            # and swap the current and next queues   
            if not current_queue:
                level_number += 1
                if next_queue:
                    print(" : ", end="")
                current_queue = queues[level_number % 2]
                next_queue = queues[(level_number + 1) % 2]
            else:
                print(", ", end="")

def main():
    # Creating a binary tree
    input1 = [100, 50, 200, 25, 75, 350]
    tree1 = BinaryTree(input1)

    # Creating a right degenerate binary tree
    input2 = sorted(input1)
    tree2 = BinaryTree(input2)

    # Creating a left degenerate binary tree
    input2.reverse()
    tree3 = BinaryTree(input2)

    # Creating a single node binary tree
    tree4 = BinaryTree(100)

    test_case_roots = [tree1.root, tree2.root, tree3.root, tree4.root, None]
    test_case_statements = ["Level-Order Traversal of a normal binary search tree: ",
            "Level-Order Traversal of a right degenerate binary search tree: ",
            "Level-Order Traversal of a left degenerate binary search tree: ",
            "Level-Order Traversal of a single node binary tree: ",
            "Level-Order Traversal of a null tree: "]

    for i in range(len(test_case_roots)):
        if (i > 0):
            print()
        print(str(i + 1) + ". Binary Tree:")
        display_tree(test_case_roots[i])
        print("\n   " + test_case_statements[i],end="\n   ")

        # Printing the in-order list using the method we just implemented
        level_order_traversal(test_case_roots[i])
        print("\n-------------------------------------------------------------------------------------------------------------------------------")

if __name__ == '__main__':
    main()