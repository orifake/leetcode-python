# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        dummy = ListNode(0)
        dummy.next = None
        h = dummy

        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                h.next = l2
                l2 = l2.next
            else:
                h.next = l1
                l1 = l1.next
            h = h.next
        if l1 is not None:
            h.next = l1 
        else:
            h.next = l2
        
        return dummy.next