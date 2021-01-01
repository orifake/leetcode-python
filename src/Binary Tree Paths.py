from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List:
        result, path = [], []
        self.dfs(root, path, result)
        return result

    def dfs(self, node: TreeNode, path: List, result: List):
        if not node:
            return
        path.append(str(node.val))
        if not node.left and not node.right:
            result.append('->'.join(path))
        if node.left:
            self.dfs(node.left, path, result)
        if node.right:
            self.dfs(node.right, path, result)
        path.pop()