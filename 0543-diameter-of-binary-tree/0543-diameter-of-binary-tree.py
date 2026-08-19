# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def  height(root):
            if root is None:
                return 0
            return 1+ max(height(root.left),height(root.right))
        def diam(root):
            if root is None:
                return 0
            currDiam=1+height(root.left)+height(root.right)
            leftDiam=diam(root.left)
            rightDiam=diam(root.right)
            return max(currDiam,leftDiam,rightDiam)
        return diam(root)-1
        