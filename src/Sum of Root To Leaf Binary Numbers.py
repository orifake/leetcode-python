# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def preorder(node, curr_sum):
            nonlocal root_to_leaf
            if node:
                curr_sum = (curr_sum << 1) | node.val
                if not (node.left or node.right):
                    root_to_leaf += curr_sum

                preorder(node.left, curr_sum)
                preorder(node.right, curr_sum)

        root_to_leaf = 0
        preorder(root, 0)

        return root_to_leaf