class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # Left child
        self.right = None  # Right child

values = []
def get_list(root):
    if not root:
        return

    get_list(root.left)
    get_list(root.right)
    values.append(root.value)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

get_list(root)
print(values)