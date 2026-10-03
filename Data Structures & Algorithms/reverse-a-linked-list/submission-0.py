# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        def dfs(node):
            if node.next == None:
                return node
            tmp = dfs(node.next) 
            node.next.next = node    
            node.next = None       
            return tmp 

        return dfs(head)