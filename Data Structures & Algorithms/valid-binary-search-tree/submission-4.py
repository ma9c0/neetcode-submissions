# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(mi, ma, node):
            if not node:
                return True
            if mi >= node.val or ma <= node.val:
                return False

            return dfs(mi, min(ma, node.val), node.left) and dfs(max(mi, node.val), ma, node.right)

        return dfs(-math.inf, math.inf, root)