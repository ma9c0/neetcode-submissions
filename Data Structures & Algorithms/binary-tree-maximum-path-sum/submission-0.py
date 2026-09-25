# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -math.inf

        def dfs(node: TreeNode):
            nonlocal max_sum
            if node == None:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            left_sum = max(0, left_sum)
            right_sum = max(0, right_sum)

            current_sum = node.val + left_sum + right_sum
            max_sum = max(current_sum, max_sum)

            return max(left_sum, right_sum) + node.val

        dfs(root)
        return max_sum