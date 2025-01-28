class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None  

values = []
def get_list(root):
    if not root:
        return
    
    values.append(root.value)
    get_list(root.left)
    get_list(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

"""
        1
       / \
      2   3
     / \
    4   5  

    1 -> [1]
    2 -> 2
"""

get_list(root)
print(values)

