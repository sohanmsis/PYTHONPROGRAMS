class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_terminal_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_terminal_nodes(root.left) + count_terminal_nodes(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Number of terminal nodes in the binary tree is:", count_terminal_nodes(root))