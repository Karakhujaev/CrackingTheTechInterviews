# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import heapq
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        values = []
        def inorder(node):
            if node:
                inorder(node.left)
                values.append(node.val)
                inorder(node.right)
        
        inorder(root)
        heapq.heapify(values)
        for _ in range(k - 1):
            heapq.heappop(values)
        
        return heapq.heappop(values)

