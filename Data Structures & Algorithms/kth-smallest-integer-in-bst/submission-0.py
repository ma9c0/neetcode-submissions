# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal k
            if not node:
                return None

            tmp = dfs(node.left)
            if tmp != None:
                return tmp
            k -= 1

            if k == 0:
                return node.val


            tmp2 = dfs(node.right)
            if tmp2 != None:
                return tmp2


        return dfs(root)