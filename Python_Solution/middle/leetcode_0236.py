"""
    1、二叉树的最近公共祖先
"""
# 2022/7/26  author:github
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else (left or right)
