from binary_tree import *
from binary_tree_node import *

# Function to check if the two trees are identical
def are_identical(root1, root2):
    # Returns true if both trees have null as root (first base case)
    if not root1 and not root2:
        return True

    # Function returns false if one of the roots here is null (second base case)
    if root1 and root2:
        # Returns true if both nodes have the same left sub-tree, right sub-tree
        # and value
        return (root1.data == root2.data and
                are_identical(root1.left, root2.left) and
                are_identical(root1.right, root2.right))

    # Returns false if neither of the above cases are satisfied
    return False


def main():
    input1 = [100, 50, 200, 25, 125, 350]
    obj1 = BinaryTree(input1)

    input2 = [4, 2, 6, 1, 5, 7]
    obj2 = BinaryTree(input2)

    input3 = [100, 25, 200, 50, 125, 350]
    obj3 = BinaryTree(input3)

    testCaseRoot1 = [obj1.root, obj1.root, obj1.root, obj1.root, None]
    testCaseRoot2 = [obj1.root, obj2.root, obj3.root, None, None]

    for i in range(len(testCaseRoot1)):
        if (i > 0):
            print("\n")

        # Displaying level-order traversal of trees being tested
        print((i + 1), ".\tLevel-Order Traversal of First Tree:  ")
        display_tree(testCaseRoot1[i])
        print("\n\tLevel-Order Traversal of Second Tree: ")
        display_tree(testCaseRoot2[i])
        print("\n\tIdentical Tree: ", end="")

        # Calling our areIdentical() function to check if tree are identical
        if are_identical(testCaseRoot1[i], testCaseRoot2[i]):
            print("true")
        else:
            print("false")
        print(
            "----------------------------------------------------------------------------------------------------\n", end="")


if __name__ == '__main__':
    main()