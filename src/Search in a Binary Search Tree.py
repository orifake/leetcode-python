# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def search(node, val):
            if not node:
                return None
            if node.val == val:
                return node

            leftNode = search(node.left, val)
            rightNode = search(node.right, val)
            return leftNode or rightNode

        return search(root, val)
