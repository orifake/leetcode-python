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

    def dfs(self, root: TreeNode, path:List, result:List):
        if not root:
            return
        path.append(str(root.val))
        if not root.left and not root.right:
            result.append('->'.join(path))
        if root.left:
            self.dfs(root.left, path, result)
        if root.right:
            self.dfs(root.right, path, result)
        path.pop()