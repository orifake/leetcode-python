# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        self.subTreeSum(root)
        return self.ans

    def subTreeSum(self, root):
        if root is None:
            return 0

        lsum = self.subTreeSum(root.left)
        rsum = self.subTreeSum(root.right)
        self.ans += abs(lsum - rsum)
        return root.val + lsum + rsum
