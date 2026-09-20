# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0

        def dfs(node, current_max):
            nonlocal res
            if not node:
                return
            if node.val >= current_max:
                res = res + 1
            
            current_max = max(node.val, current_max)
            dfs(node.left, current_max)
            dfs(node.right, current_max)

        dfs(root, root.val)
        return res