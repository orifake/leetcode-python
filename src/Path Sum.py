# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            if sum == root.val:
                return True
            else:
                return False
        left = False
        right = False
        if root.left:
            left = self.hasPathSum(root.left, sum - root.val)
        if root.right:
            right = self.hasPathSum(root.right, sum - root.val)
        return left or right
