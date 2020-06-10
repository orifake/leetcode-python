# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def isMirror(a, b):
            if a == None and b == None:
                return True
            if a == None or b == None:
                return False
            return a.val == b.val and isMirror(a.left, b.right) and isMirror(
                a.right, b.left)

        return isMirror(root.left, root.right)
