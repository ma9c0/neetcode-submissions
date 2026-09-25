# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum = 0

        def dfs(node, cur):
            nonlocal sum
            if node == None:
                return 0
            cur = cur * 10 + node.val
            if not node.left and not node.right:
                return cur 
            return dfs(node.left, cur) + dfs(node.right, cur)

        return dfs(root, 0)