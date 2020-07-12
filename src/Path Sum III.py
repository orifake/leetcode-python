# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(
            root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, root, sum):
        # count the number of paths starting from the node
        ans = 0
        if not root:
            return ans
        if root.val == sum:
            ans += 1
        ans += self.dfs(root.left, sum - root.val)
        ans += self.dfs(root.right, sum - root.val)
        return ans