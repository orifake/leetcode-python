# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def isSame(a, b):
            if a == None and b == None:
                return True
            if a == None and b != None:
                return False
            if a != None and b == None:
                return False
            if a.val == b.val:
                return True
            return False

        deq = deque([
            (p, q),
        ])
        while deq:
            p, q = deq.popleft()
            if not isSame(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True