# Class representing a single node in a binary tree
class TreeNode:
    # Initializes a node with a given value
    def __init__(self, value):
        self.value = value  # node value
        self.left = None    # reference to the left child node
        self.right = None   # reference to the right child node


# Class implementing a binary tree data structure
class BinaryTree:
    # Initializes the binary tree with a root node containing the given value
    def __init__(self, root_value):
        self.root = TreeNode(root_value)  # root node of the tree

    # Method to insert a new node with the given value into the binary tree
    def insert(self, value):
        self._insert_recursively(self.root, value)

    # Recursive method to insert a new node into the binary tree
    def _insert_recursively(self, node, value):
        # If the value to insert is less than the current node's value,
        # go to the left subtree
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        # If the value to insert is greater than or equal to the current node's value,
        # go to the right subtree
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    # Method to perform an inorder traversal of the binary tree
    def inorder_traversal(self, node):
        if node:
            # Traverse the left subtree
            self.inorder_traversal(node.left)
            # Visit the current node
            print(node.value, end=" ")
            # Traverse the right subtree
            self.inorder_traversal(node.right)

    # Method to perform a preorder traversal of the binary tree
    def preorder_traversal(self, node):
        if node:
            # Visit the current node
            print(node.value, end=" ")
            # Traverse the left subtree
            self.preorder_traversal(node.left)
            # Traverse the right subtree
            self.preorder_traversal(node.right)

    # Method to perform a postorder traversal of the binary tree
    def postorder_traversal(self, node):
        if node:
            # Traverse the left subtree
            self.postorder_traversal(node.left)
            # Traverse the right subtree
            self.postorder_traversal(node.right)
            # Visit the current node
            print(node.value, end=" ")


# Example usage of the BinaryTree class
if __name__ == "__main__":
    # Create a binary tree with root value 10
    tree = BinaryTree(10)

    # Insert some values into the binary tree
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(8)
    tree.insert(12)
    tree.insert(18)

    # Perform inorder traversal (prints the values in sorted order)
    print("Inorder traversal:")
    tree.inorder_traversal(tree.root)
    print()

    # Perform preorder traversal
    print("Preorder traversal:")
    tree.preorder_traversal(tree.root)
    print()

    # Perform postorder traversal
    print("Postorder traversal:")
    tree.postorder_traversal(tree.root)
    print()
