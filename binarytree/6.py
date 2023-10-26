class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_descending(root):
    if root is None:
        return

    stack = []
    current = root

    while True:
        if current is not None:
            stack.append(current)
            current = current.right
        elif stack:
            node = stack.pop()
            print(node.val, end=" ")
            current = node.left
        else:
            break



root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

print("Nodes in descending order are:")
traverse_descending(root)
