# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        val = root.val
        valP = p.val
        valQ = q.val
        if root == None or root == p or root == q:
            return root

        if val > valP and val > valQ:
            return self.lowestCommonAncestor(root.left, p, q)
        elif val < valP and val < valQ:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
