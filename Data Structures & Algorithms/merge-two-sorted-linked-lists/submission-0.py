# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        cur = None
        if not list1:
            return list2
        elif not list2:
            return list1
        elif not list1 and not list2:
            return None

        while list1 or list2:
            if cur == None:
                if list1.val < list2.val:
                    cur = list1
                    list1=list1.next
                else:
                    cur = list2
                    list2=list2.next
                head=cur
            elif not list1 and list2:
                cur.next = list2
                list2 = list2.next
                cur=cur.next
            elif not list2 and list1:
                cur.next = list1
                list1 = list1.next
                cur=cur.next
            elif list1.val < list2.val:
                cur.next = list1
                list1=list1.next
                cur=cur.next
            else:
                cur.next=list2
                list2=list2.next
                cur=cur.next

        return head
            

            