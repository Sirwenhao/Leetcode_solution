"""
    1、二叉树中序遍历
    2、中序遍历顺序：左中右
"""
# 2022/7/18  author:WH
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Solution:
    def inorderTraversal(self, root):
        ans = []
        def traversal(root):
            if root == None:
                return
            traversal(root.left)
            ans.append(root.val)
            traversal(root.right)
        traversal(root)
        return ans