# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find root that matches the root of the substree and do dfs on both to see if it matches

        def find_root(n1, subRoot):
            if n1 == None:
                return False
            if n1.val == subRoot.val and check_contains(n1, subRoot):
                return True
            else:
                return find_root(n1.left, subRoot) or find_root(n1.right, subRoot)
                    
        def check_contains(r1, sub_r) -> bool:
            # given two roots check if all of the descendants matches 
            if r1 == None and sub_r == None:
                return True
            if r1 == None or sub_r == None or r1.val != sub_r.val:
                return False
            return check_contains(r1.left, sub_r.left) and check_contains(r1.right, sub_r.right)

        return find_root(root, subRoot)
