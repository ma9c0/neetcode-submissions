# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None:
            return None
        fast, slow = head, head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        # slow = mid point, end of the first half
        second = slow.next
        slow.next = None
        prev = None
        cur = second
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        second = prev
        while second :
            tmp1 = head.next
            tmp2 = second.next
            head.next = second
            second.next = tmp1
            head = tmp1
            second = tmp2

