# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculatehight(self,root):
        if not root:
            return 0
        l_h=self.calculatehight(root.left)
        r_h = self.calculatehight(root.right)


        self.diameter = max(self.diameter,l_h+r_h)

        return 1+max(l_h,r_h)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        self.calculatehight(root)

        return self.diameter
