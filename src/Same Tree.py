# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True

        if p is not None and q is not None:
            return p.val == q.val and self.isSameTree(
                p.left, q.left) and self.isSameTree(p.right, q.right)

        return False

class Solution2:
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