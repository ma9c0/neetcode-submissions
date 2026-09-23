# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        look_up = {val: index for index, val in enumerate(inorder)}
        def helper(pre, ino):
            if pre[0] == pre[1] or ino[0] == ino[1] or pre[0] >= len(preorder):
                return None

            node_val = preorder[pre[0]]
            node_idx = look_up[node_val] - ino[0]

            left = [ino[0], node_idx + ino[0]]
            right = [node_idx + ino[0]+1, ino[1]]
            pre_left = [pre[0] + 1, node_idx + pre[0]+1]
            pre_right = [node_idx + pre[0]+ 1, pre[1]]

            node = TreeNode(val=node_val, left=helper(pre_left, left), right=helper(pre_right, right))
            return node


        return helper([0, len(preorder)], [0, len(preorder)])