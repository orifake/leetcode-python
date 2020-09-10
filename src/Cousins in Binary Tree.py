import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.m = collections.defaultdict(tuple)
        print(self.m)

        def dfs(node, parent, depth):
            if node:
                self.m[node.val] = (parent, depth)
                dfs(node.left, node, depth + 1)
                dfs(node.right, node, depth + 1)

        dfs(root, None, 0)
        px, dx = self.m[x]
        py, dy = self.m[y]
        return dx == dy and px != py