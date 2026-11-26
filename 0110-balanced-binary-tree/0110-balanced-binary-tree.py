class Solution:
    def solve(self, root):
        if not root:
            return 0

        l_h = self.solve(root.left)
        if l_h == -1:
            return -1

        r_h = self.solve(root.right)
        if r_h == -1:
            return -1

        if abs(l_h - r_h) > 1:
            return -1

        return 1 + max(l_h, r_h)

    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.solve(root) != -1