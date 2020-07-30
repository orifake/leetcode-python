# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        return self.find(root, k, s)

    def find(self, root, k, s):
        if not root:
            return

        if k - root.val in s:
            return True

        s.add(root.val)
        return self.find(root.left, k, s) or self.find(root.right, k, s)
