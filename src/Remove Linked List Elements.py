# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0)  #头节点
        dummy.next = head
        preNode = dummy  #当前节点的上一个节点
        currentNode = dummy.next
        while currentNode is not None:
            if currentNode.val == val:
                preNode.next = currentNode.next
                currentNode = currentNode.next
            else:
                preNode = preNode.next
                currentNode = currentNode.next

        return dummy.next
