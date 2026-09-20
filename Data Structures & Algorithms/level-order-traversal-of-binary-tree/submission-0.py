# Definition for a binary tree node.
# class TreeNode:
#     def __init__(DefaultDict, self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            tmp = deque([root])
            res = [[root.val]]
        else:
            return []
        
        while tmp:
            level = []
            for _ in range(len(tmp)):
                r = tmp.popleft()
                if r.left:
                    level.append(r.left.val)
                    tmp.append(r.left)
                if r.right:
                    tmp.append(r.right)
                    level.append(r.right.val)
            if level != []:
                res.append(level) 
            
        return res

        