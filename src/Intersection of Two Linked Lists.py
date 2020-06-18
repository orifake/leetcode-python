# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None

        pointer_A = headA
        pointer_B = headB

        while pointer_A != pointer_B:
            pointer_A = headB if pointer_A == None else pointer_A.next
            pointer_B = headA if pointer_B == None else pointer_B.next

        return pointer_A