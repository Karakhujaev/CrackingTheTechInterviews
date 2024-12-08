# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        def dfs(node):
            if node is None:
                return []
            
            result = []
            # Traverse left subtree
            result.extend(dfs(node.left))
            # Traverse right subtree
            result.extend(dfs(node.right))
            # Visit the root node
            result.append(node.val)
            
            return result
        
        # Start the recursive postorder traversal
        return dfs(root)