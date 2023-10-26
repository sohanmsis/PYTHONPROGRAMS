class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of tree is %d" % height(root))