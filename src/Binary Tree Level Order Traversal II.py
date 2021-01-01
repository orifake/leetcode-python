# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.order(root, result, 0)
        return result[::-1]

    def order(self, node, result, level):
        if not node:
            return
        if level >= len(result):
            result.append([])
        result[level].append(node.val)
        self.order(node.left, result, level + 1)
        self.order(node.right, result, level + 1)