# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        stack = deque([[root]])
        level = 0

        while len(stack) > 0:
            tmp = []
            for node in stack.popleft():
                if node:
                    tmp.append(node.left)
                    tmp.append(node.right)
            level += 1
            if tmp != []:
                stack.append(tmp) 

        return level -1 