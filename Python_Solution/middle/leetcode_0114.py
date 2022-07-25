"""
    1、二叉树展开为链表
"""
# 2022/7/25  author:WH
class Solution:
    def flatten(self, root):
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
            root = root.right