# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = 0
        if root.left and self.isLeaf(root.left):
            result += root.left.val
        return result + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(
            root.right)

    def isLeaf(self, root: TreeNode):
        if root.left == None and root.right == None:
            return True