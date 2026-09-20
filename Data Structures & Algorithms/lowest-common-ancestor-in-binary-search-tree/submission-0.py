# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        l = q if q.val > p.val else p
        s = q if l == p else p
        while True:
            if root.val >= s.val and root.val <= l.val:
                return root
            elif root.val > l.val:
                root = root.left
            else:
                root = root.right