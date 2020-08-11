# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if root is None:
            return
        
        temp = []
        node = self.inorder(root, temp)
        minimum = min([abs(node[i + 1] - node[i]) for i in range(len(node) - 1)])
        return minimum

    def inorder(self,root,temp):
        if root == None:
            return
        self.inorder(root.left, temp)
        temp.append(root.val)
        self.inorder(root.right, temp)
        return temp
