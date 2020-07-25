# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(a, b):
            if not a or not b:
                return not a and not b
            if a.val == b.val and dfs(a.left, b.left) and dfs(
                    a.right, b.right):
                return True
            if b is t:
                return dfs(a.left, t) or dfs(a.right, t)
            return False

        return dfs(s, t)
